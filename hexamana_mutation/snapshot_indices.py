import numpy as np
import os
GMVAE_initlabels=np.load("labels_GMVAE.npy")

def hbond_saltbridge(GMVAE_labels, hbond_list, hbond_residues, salt_list, salt_residues):
    max_label=np.max(GMVAE_labels)
    label_values=np.zeros(hbond_list.shape[1])
    hbond_list=hbond_list[:,1:]
    hbond_list=np.transpose(hbond_list)
    salt_list=np.transpose(salt_list)
    total_bonds= np.concatenate((hbond_list, salt_list), axis=1)
    total_residues= np.concatenate((hbond_residues,salt_residues))
    total_bonds = total_bonds.astype(int)
   
    for l in range(0,max_label+1):
        label_values=np.zeros(total_bonds.shape[1])
        positions=np.where(GMVAE_labels == l)[0]
        len_occur=np.sum(GMVAE_labels == l)
        if len_occur > 0:
            print("fraction",len_occur/7501)
            for k in range (0,total_bonds.shape[1]):
                combined_data=total_bonds[:,k][positions]
                if (combined_data.shape[0]>0):
                    max_occ=np.bincount(combined_data).argmax()
                    label_values[k]=max_occ
            combined_values = np.tile(label_values, (len_occur, 1))
            important_data=total_bonds[positions,:]
            difference_array=combined_values-important_data
            abs_array = np.abs(difference_array)
            row_sum = np.sum(abs_array, axis=1)
            min_row_sum_indices = np.where(row_sum == np.min(row_sum))[0]
            min_pos = min_row_sum_indices[0]
            print ("label",l,"positions",positions[min_pos],"total_bonds",total_bonds[positions[min_pos],:],"total_residues",total_residues,"minimum_sum",np.min(row_sum))
        

os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/tetraha_mutation/tetraha/H123/gromacs")
hbond_list=np.load("h_bondlist.npy")
hbond_residues=np.load("h_residues.npy")
salt_bridge=np.load("salt_bridge.npy")
salt_list=np.load("salt_list.npy")
GMVAE_labels=GMVAE_initlabels[0:7501]
print ("tetraha_H123")
hbond_saltbridge(GMVAE_labels,hbond_list,hbond_residues,salt_bridge,salt_list)
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/tetraha_mutation/tetraha/NOH123/gromacs")
hbond_list=np.load("h_bondlist.npy")
hbond_residues=np.load("h_residues.npy")
salt_bridge=np.load("salt_bridge.npy")
salt_list=np.load("salt_list.npy")
GMVAE_labels=GMVAE_initlabels[7501:15002]
print ("tetraha_NOH123")
hbond_saltbridge(GMVAE_labels,hbond_list,hbond_residues,salt_bridge,salt_list)
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/tetraha_mutation/H221F_tetraha/H123/gromacs")
hbond_list=np.load("h_bondlist.npy")
hbond_residues=np.load("h_residues.npy")
salt_bridge=np.load("salt_bridge.npy")
salt_list=np.load("salt_list.npy")
GMVAE_labels=GMVAE_initlabels[15002:15002+7501]
print ("H221F_tetraha_H123")
hbond_saltbridge(GMVAE_labels,hbond_list,hbond_residues,salt_bridge,salt_list)
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/biochemistry_mutation/tetraha_mutation/H221F_tetraha/H123/gromacs")
hbond_list=np.load("h_bondlist.npy")
hbond_residues=np.load("h_residues.npy")
salt_bridge=np.load("salt_bridge.npy")
salt_list=np.load("salt_list.npy")
print ("H221F_tetraha_NOH123")
GMVAE_labels=GMVAE_initlabels[15002+7501:15002+7501*2]
hbond_saltbridge(GMVAE_labels,hbond_list,hbond_residues,salt_bridge,salt_list)
