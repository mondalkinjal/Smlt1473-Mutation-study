silly_cutoff=0.4
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
from itertools import islice
ligands=["fourha","tetraha","hexamana"]
#an=["rmsd","energy","protein_ligand_contact"]
an=["h_bonds","salt_bridges"]
file1 = open("outputscoredis.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()

for ligand in ligands:
    if ligand=="tetraha":
        clus_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation"
        set1_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/tetraha/correct_set/h_123/gromacs"
        set2_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/tetraha/correct_set/no_h_123/gromacs"
        set3_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/H221F_tetraha/correct_set/h_123/gromacs"
        set4_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/H221F_tetraha/correct_set/no_h_123/gromacs"
        sets=[set1_dir,set2_dir,set3_dir,set4_dir]
    if ligand=="fourha":
        clus_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation"
        set1_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs"
        set2_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/noh_123/gromacs"
        set3_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/H221F_fourha_beta/h_123/gromacs"
        set4_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/H221F_fourha_beta/noh_123/gromacs"
        sets=[set1_dir,set2_dir,set3_dir,set4_dir]
    if ligand=="hexamana":
        clus_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations"
        set1_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/hexamana/correct_set/h_109/gromacs"
        set2_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/hexamana/correct_set/no_h_109/gromacs"
        set3_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/H221F_hexamana/correct_set/h_109/gromacs"
        set4_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/H221F_hexamana/correct_set/no_h_109/gromacs"
        set5_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/R312L_hexamana/correct_set/h_109/gromacs"
        set6_dir="/expanse/lustre/projects/mda123/kmondal/fresh_folder/hexamana_all_mutations/R312L_hexamana/correct_set/no_h_109/gromacs"
        sets=[set1_dir,set2_dir,set3_dir,set4_dir,set5_dir,set6_dir]
    #os.chdir(clus_dir)
    

    for fun in an:
        print (fun)
        if fun=="h_bonds" or fun=="salt_bridges":
            #final_i=int(len(sets)/2)+1
            final_i=int(len(sets))+1

            for i in range(1,final_i):
                os.chdir(sets[i-1])
                if fun=="h_bonds":
                    func_values=np.load("h_bondlist.npy")
                    
                    func_values=func_values[:,1:]
                    func_values=np.transpose(func_values)
                    func_values = func_values.astype(int)
                    #print (func_values.shape)
                if fun=="salt_bridges":
                    func_values=np.load("salt_bridge.npy")
                    func_values=np.transpose(func_values)
                    func_values = func_values.astype(int)
                    #print (func_values.shape)
                labels=["GMVAE","kmeans"]    
                for label in labels:
                    os.chdir(clus_dir)
                    os.getcwd()
                    #print(ligand)
                    filename=f"labels_{label}.npy"
                    #print (filename)
                    lab=np.load(filename)
                    #print (lab.shape) 
                    lab=lab[(i-1)*7501:(i)*7501]
                    max_label=np.max(lab)
                    #print ("max_label",max_label)
                    final_score=0
                    for k in range(0,func_values.shape[1]):
                        for l in range(0,max_label+1):

                            positions=np.where(lab == l)
                            len_occur=np.sum(lab==l)
                            #print(len_occur)
                            #print(len(lab))
                            frac_positions = len_occur/len(lab)
                            if fun=="salt_bridges" or fun=="h_bonds":
                                combined_data=func_values[:,k][positions]
                                #print (l,combined_data.shape)
                                if (combined_data.shape[0]>0):

                                    max_occ_count=np.bincount(combined_data).max()
                                    total_elements=len(combined_data)
                                    frac_occ=(max_occ_count/total_elements)
                                #print (frac_occ,frac_positions,"yeah")
                                    final_score=final_score+frac_positions*frac_occ
                    final_score=final_score/(func_values.shape[1])   
                    os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation")
                    file1 = open("outputscoredis.txt", "a")  # append mode
                    file1.write(f'{ligand},{label},{final_score},{fun}\n')
                    file1.close()
                    print (ligand,label,final_score,fun)
                    

                
            


