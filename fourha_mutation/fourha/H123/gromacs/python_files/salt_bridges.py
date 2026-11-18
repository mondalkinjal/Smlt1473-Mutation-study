
#import numpy as np
#directory_path ="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs/saltbridges"
#ois.chdir(directory_path)
#threshold=3.5
#fraction_threshold=0.20
#l=[]
#for file_name in file_list:
    
#    end_name=file_name[-3:]
#    if (end_name=='dat'):
#        data=np.loadtxt(file_name)
#        x_data = data[:, 0]  # First column (X)
#        y_data = data[:, 1]  # Second column (Y)
#        mask = data < threshold
#        count = np.count_nonzero(mask)
#        length=len(y_data)
#        if ((count/length)>fraction_threshold):
#            l.append(file_name)
#print (l)
import MDAnalysis as mda
import MDAnalysis.analysis.distances import dist
from collection import Counter
u=mda.Universe("protein_ligand.gro","final_production.xtc")
cutoff=3.5
u1=u.select_atoms("(resname ARG and (name NE or name NH1 or name NH2)) or (resname LYS and name NZ) or (resname HSP and (name NE2 or name ND1))")
k=u1.resids
distinct_count=len(set(k))
element_count=Counter(k)
final_matrix=np.zeros(distinct_count,len(u.trajectory))
for i in range (0,len(u.trajectory)):
    u1=u.select_atoms("(resname ARG and (name NE or name NH1 or name NH2)) or (resname LYS and name NZ) or (resname HSP and (name NE2 or name ND1))")
    u2=u.select_atoms("resname BGLCA and (name 061 or name 062)") 
    k=u1.resids
    element_count=Counter(k)
    sorted_keys=sorted(element_count.keys())
    sorted_dict={key:element_count[key] for key in sorted_keys}
    key_values=[sorted_dict[key] for key in sorted_dict]
    dist_arr=mda.analysis.distances.distance_array(u1.positions,u2.positions,box=[78.80383,78.80383,78.80383,90.,90.,90.])
    #print (dist_arr.shape)
    result_arr= np.where(dist_arr<cutoff)
    sum_result_arr=np.sum(result_arr, axis=0)
    p=0
    #s=0
    for j in range (0,element_count):
        final_matrix[j,i]=np.sum(sum_result_arr[p:p+key_values[j])
        p=p+key_values[j]
np.save("salt_bridge.npy",final_matrix)
np.save("resid_list.npy",k)
