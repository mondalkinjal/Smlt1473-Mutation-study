import pandas as pd
import re
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches

# Define the list of .pka files in the correct order
pka_files = [
    "Smlt_cleaned.pka", 
    "Smlt_H221F.pka",
    "Smlt_R312L.pka"
]  # Replace with your actual file names

# List of files where residue numbers should be increased by 21
files_need_offset = ["Smlt_H221F.pka","Smlt_R312L.pka"]  # Customize this list

# Residue mapping for single-letter codes
residue_map = {
    "ASP": "D", "GLU": "E", "HIS": "H", "LYS": "K", "ARG": "R",
    "SER": "S", "THR": "T", "ASN": "N", "GLN": "Q", "CYS": "C",
    "GLY": "G", "PRO": "P", "ALA": "A", "VAL": "V", "ILE": "I",
    "LEU": "L", "MET": "M", "PHE": "F", "TYR": "Y", "TRP": "W"
}

# Modified function with apply_offset logic
def extract_pka_data(file_path, apply_offset=False):
    extracted_data = []
    inside_summary = False
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            
            if "SUMMARY OF THIS PREDICTION" in line:
                inside_summary = True
                continue
            
            if inside_summary and re.match(r"^-{5,}", line):
                break
            
            if inside_summary and line:
                parts = line.split()
                if len(parts) >= 3:
                    residue, number, chain = parts[0], parts[1], parts[2]
                    pka_value = parts[3]
                    
                    try:
                        if apply_offset:
                            new_number = int(number) + 21
                        else:
                            new_number = int(number)
                        one_letter_residue = residue_map.get(residue, "?")
                        residue_code = f"{one_letter_residue}{new_number}"
                        extracted_data.append([residue_code, pka_value])
                    except ValueError:
                        continue  

    df = pd.DataFrame(extracted_data, columns=["Residue", file_path])
    return df

# Process files with offset logic
dfs = []
for file in pka_files:
    apply_offset = file in files_need_offset  # Determine if offset is needed
    df = extract_pka_data(file, apply_offset=apply_offset)
    dfs.append(df)

# Merge all DataFrames on "Residue"
merged_df = dfs[0]
for df in dfs[1:]:
    merged_df = pd.merge(merged_df, df, on="Residue", how="outer")

# Rename columns using file names (remove ".pka" from headers)
column_mapping = {file: file.replace(".pka", "") for file in pka_files}
merged_df.rename(columns=column_mapping, inplace=True)

# Function to set gridlines for the Word table
def set_table_borders(table):
    tbl = table._tbl
    tblBorders = OxmlElement('w:tblBorders')
    
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '4')
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), '000000')
        tblBorders.append(border)
    
    tbl.append(tblBorders)

# Function to write DataFrame to Word
def write_df_to_word(df, output_path):
    doc = Document()
    table = doc.add_table(rows=1, cols=len(df.columns))
    
    table.autofit = False

    for col in table.columns:
        for cell in col.cells:
            cell.width = Inches(0.8)

    set_table_borders(table)

    for i, col in enumerate(df.columns):
        table.cell(0, i).text = col

    for _, row in df.iterrows():
        row_cells = table.add_row().cells
        for i, value in enumerate(row):
            if i == 0:
                row_cells[i].text = str(value)
            else:
                # Try converting to float and format with three significant figures
                try:
                    num_val = float(value)
                    formatted_val = format(num_val, '.3g')
                except ValueError:
                    formatted_val = str(value)
                row_cells[i].text = formatted_val
            row_cells[i].width = Inches(0.2)
    doc.save(output_path)

# Save to Word document
write_df_to_word(merged_df, 'merged_pka_table.docx')

print("pKa files merged and saved as 'merged_pka_table.docx'")
