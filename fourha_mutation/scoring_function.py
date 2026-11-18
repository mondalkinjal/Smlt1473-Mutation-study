silly_cutoff=0.4
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
from itertools import islice
ligands=["tetraha","hexamana","fourha"]
an=["rmsd","energy","protein_ligand_contact"]
#an=["h_bonds","salt_bridges"]
file1 = open("outputscore.txt", "w")
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
        final_i=int(len(sets)/2)+1
        for i in range(1,final_i):
            func=[]
            for j in range(0,2):
                set_no=2*(i-1)+j
                os.chdir(sets[set_no])
                
                if fun=="rmsd":
                    print (os.getcwd())
                    rmsd=np.load("final_rmsd.npy")
                    func.append(rmsd)
                    func[j]=func[j].reshape(-1, 1)
                    print (func[j].shape)
                if fun=="energy":
                    filename = "energy_protein_ligand.xvg"
                    with open(filename, 'r') as file:
                        energy = np.loadtxt(islice(file, 27, None))
                        func.append(energy)
                        func[j] = func[j][:,1:]
                if fun=="protein_ligand_contact":
                    contact=np.load("protein_ligand_contact.npy")
                    func.append(contact)
                    func[j]=np.transpose(func[j])
            func_values=np.concatenate((func[0],func[1]), axis=0)
            labels=["GMVAE","kmeans"]    
            for label in labels:
                os.chdir(clus_dir)
                filename=f"labels_{label}.npy"
                lab=np.load(filename)
        
                lab=lab[(2*i-2)*7501:(2*i)*7501]
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
                        if fun=="rmsd" or fun=="energy" or fun=="protein_ligand_contact":
                            combined_data=func_values[:,k][positions]
                            if (combined_data.shape[0]>0):
                                combined_data=combined_data.reshape(-1,1)
                                def silly(k,combined_data):
                                    if (combined_data.shape[0]>k):
                                        kmeans=KMeans(n_clusters=k)
                                        kmeans.fit(combined_data)
                                        final_label=kmeans.predict(combined_data)
                                        print ("yeah,error_final_label")
                                        are_all_elements_same = np.all(final_label == final_label[0])
                                        if are_all_elements_same:
                                            return 0
                                        else:
                                            sc=silhouette_score(combined_data, final_label)
                                            return sc
                                    else:
                                        return 0
                            
                            
                                no=[]
                                score=[]
                                for j in range(2,10):
                                    sc=silly(j,combined_data)
                                    score.append(sc)
                                    no.append(j)
                                max_element=max(score)
                                max_index=score.index(max_element)
                                m_index=max_index+2
                                if ((m_index==2 or m_index>2)  and max(score)>silly_cutoff):
                                    m_index=m_index
                                    kmeans=KMeans(n_clusters=m_index)
                                    clusters = kmeans.fit(combined_data)
                                    max_occ_count = np.bincount(clusters.labels_).max()
                                    total_elements = len(clusters.labels_)
                                    frac_occ = (max_occ_count/total_elements)
                                    part_score=frac_positions*frac_occ
                                    final_score=final_score+part_score
                            #elif (m_index>2):
                            #    m_index=m_index
                            #    kmeans=KMeans(n_clusters=m_index)
                            #    clusters = kmeans.fit(combined_data)
                            #    max_occ_count = np.bincount(clusters.labels_).max()
                            #    total_elements = len(clusters.labels_)
                            #    frac_occ = (max_occ_count/total_elements)
                            #    part_score=frac_positions*frac_occ
                            #    final_score=final_score+part_score
                                else:
                                    m_index=1
                                    final_score=final_score+frac_positions        
                        
                final_score=final_score/(func_values.shape[1])    
                os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation")
                file1 = open("outputscore.txt", "a")  # append mode
                file1.write(f'{ligand},{label},{final_score},{fun}\n')
                file1.close()
                print (ligand,label,final_score,fun)

                
            


