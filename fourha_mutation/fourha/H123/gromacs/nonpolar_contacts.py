
import MDAnalysis as mda
from MDAnalysis.analysis.distances import dist
from collections import Counter
import numpy as np
u=mda.Universe("protein_ligand.gro","final_production.xtc")
cutoff=6.5
u1=u.select_atoms("(protein and not name H*)")
print (len(u1))
k=u1.resids
distinct_count=len(set(k))
element_count=Counter(k)
final_matrix=np.zeros((distinct_count,len(u.trajectory)))
for i in range (0,len(u.trajectory)):
    u.trajectory[i]
    u1=u.select_atoms("(protein and not name H*)")
    u2=u.select_atoms("(resname BGLCA or resname BGLCN) and (not name H*)") 
    k=u1.resids
    #print ("resids",k)
    element_count=Counter(k)
    sorted_keys=sorted(element_count.keys())
    sorted_dict={key:element_count[key] for key in sorted_keys}
    #print ("sorted_dict",sorted_dict)
    key_values=[sorted_dict[key] for key in sorted_dict]
    dist_arr=mda.analysis.distances.distance_array(u1.positions,u2.positions,box=[78.80383,78.80383,78.80383,90.,90.,90.])
    #print ("dist_arr",dist_arr)
    result_arr= np.where(dist_arr<cutoff,1,0)
    #print ("result_arr",result_arr)
    sum_result_arr=np.sum(result_arr, axis=1)
    #print ("sum_result_arr",sum_result_arr)
    p=0
    #s=0
    for j in range (0,len(sorted_dict)):
        #print (sum_result_arr[p:p+key_values[j]]),
        final_matrix[j,i]=np.sum(sum_result_arr[p:p+key_values[j]])
        #print (key_values[j]),
        p=p+key_values[j]
        #print (p)
    #print (final_matrix[:,i])

#print (final_matrix)
threshold=6000
final_matrix[final_matrix>0]=1
column_sums = np.sum(final_matrix, axis=1)
print (column_sums)
# Create a mask for columns that have a sum greater than or equal to the threshold
mask = column_sums >= threshold

# Extract the columns that meet the criteria
filtered_matrix = final_matrix[mask, :]

# Get the column numbers from the original matrix whose sums are greater than the threshold
selected_columns = np.where(mask)[0]

# Print the results
#print("Original Matrix:")
#print(matrix)

#print("Filtered Matrix:")
#print(filtered_matrix)

for i in range (0,len(u.trajectory)):
    print (filtered_matrix[:,i])
print("Column Numbers with Sums >= Threshold:", selected_columns)    

print (filtered_matrix)
residue_codes=[]
#for i in range (0,distinct_count):
for residue in selected_columns:
    selection_2="resid "+str(residue)
    u2=u.select_atoms(selection_2)
    resname=u2.residues.resnames[0]
    final_string=str(resname)+str(residue)
    residue_codes.append(final_string)
print (residue_codes)

print (np.max(filtered_matrix))

np.save("nonpolar_matrix.npy",filtered_matrix)
np.save("nonpolar_list.npy",selected_columns)
