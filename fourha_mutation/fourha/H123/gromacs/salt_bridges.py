
import MDAnalysis as mda
from MDAnalysis.analysis.distances import dist
from collections import Counter
import numpy as np
u=mda.Universe("protein_ligand.gro","final_production.xtc")
cutoff=3.5
u1=u.select_atoms("(resname ARG and (name NE or name NH1 or name NH2)) or (resname LYS and name NZ) or (resname HSP and (name NE2 or name ND1))")
k=u1.resids
distinct_count=len(set(k))
element_count=Counter(k)
sorted_k=sorted(element_count.keys())

final_matrix=np.zeros((distinct_count,len(u.trajectory)))
for i in range (0,len(u.trajectory)):
    u.trajectory[i]
    u1=u.select_atoms("(resname ARG and (name NE or name NH1 or name NH2)) or (resname LYS and name NZ) or (resname HSP and (name NE2 or name ND1))")
    u2=u.select_atoms("resname BGLCA and (name O61 or name O62)") 
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
    #dist_arr[dist_arr>cutoff]=0
    #print (dist_arr)
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

print (final_matrix)
final_matrix[final_matrix>0]=1
import_indices=[]
imp_residues=[]
residue_codes=[]
cutoff=1000
for i in range (0,distinct_count):
    if (np.sum(final_matrix[i,:])>cutoff):
        imp_residues.append(sorted_k[i])
        import_indices.append(i)

important_matrix=np.zeros((len(imp_residues),len(u.trajectory)))
for i in range (0,len(imp_residues)):
    important_matrix[i,:]=final_matrix[import_indices[i],:]
    print (np.sum(important_matrix[i,:]))
    print (important_matrix[i,:])
    print (i,imp_residues[i])
for residue in imp_residues:
        selection_2="resid "+str(residue)
        u2=u.select_atoms(selection_2)
        resname=u2.residues.resnames[0]
        final_string=str(resname)+str(residue)
        residue_codes.append(final_string)
print (residue_codes)

np.save("salt_bridge.npy",important_matrix)
np.save("salt_list.npy",imp_residues)
