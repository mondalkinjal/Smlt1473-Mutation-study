import os
import MDAnalysis as mda 
import numpy as np
u=mda.Universe("protein_ligand.gro","final_production.xtc")
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/hexamana_mutation/H221F_hexamana/NOH109/gromacs/hbonds")
cutoff=1000
residues=[]
residue_codes=[]
for i in range (1,308):
    file_name = f"{i}.dat"
    data=np.loadtxt(file_name)
    second_column=data[:,1]
    second_column[second_column>0]=1
    no_bonds=np.sum(second_column)
    if (no_bonds>cutoff):
        residues.append(i)
for residue in residues:
        selection_2="resid "+str(residue)
        u2=u.select_atoms(selection_2)
        resname=u2.residues.resnames[0]
        final_string=str(resname)+str(residue)
        residue_codes.append(final_string)
print (residue_codes)

#print (residues)
#import MDAnalysis as mda
#import numpy as np
#import pandas as pd
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
h_bondlist=np.zeros((len(residues), len(u.trajectory)+1))

for i in range (0,len(residues)):
    file_name = f"{residues[i]}.dat"
    data=np.loadtxt(file_name)
    second_column=data[:,1]
    second_column[second_column>0]=1
    print (np.max(second_column))
    print (second_column.shape)
    h_bondlist[i,:]=second_column
print (np.max(h_bondlist))
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/hexamana_mutation/H221F_hexamana/NOH109/gromacs")
np.save("h_bondlist.npy",h_bondlist)
np.save("h_residues.npy",residue_codes) 
