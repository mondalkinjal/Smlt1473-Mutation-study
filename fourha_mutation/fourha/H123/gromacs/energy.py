import numpy as np
import os
from itertools import islice
#os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs")
GMVAE_data = np.load('labels_GMVAE.npy')
KMean_data = np.load('labels_kmeans.npy')
def calculate_ener(dir1,dir2,labels):
    #os.chdir(dir1)
    filename = "energy_protein_ligand.xvg"
    os.chdir(dir1)
#column1 = data[:, 0]
    print (os.getcwd())
#column2 = data[:, 1]
    with open(filename, 'r') as file:
        data = np.loadtxt(islice(file, 27, None))
    dataen1 = data[:, 1]
    dataen2 = data[:, 2]
    os.chdir(dir2)
    print (os.getcwd())
    with open(filename, 'r') as file:
        newdata = np.loadtxt(islice(file, 27, None))
    dataenr1 = newdata[:,1]
    dataenr2 = newdata[:,2]
    datax = np.concatenate((dataen1, dataenr1), axis=0)
    datay = np.concatenate((dataen2, dataenr2), axis=0)
    datat = datax + datay
    max_label=np.max(labels)
    avg=[]
    
    for i in range (1,max_label+1):

        positions = np.where(labels == i)
        value=np.average([positions])
        avg.append(value)
    return (avg)
dir1="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs"
dir2="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/noh_123/gromacs"
GMVAE_labels=GMVAE_data[:2*7501]
KMean_labels=KMean_data[:2*7501]
GMVAE_ener_wt=calculate_ener(dir1,dir2,GMVAE_labels)
KMean_ener_wt=calculate_ener(dir1,dir2,GMVAE_labels)
dir1="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/H221F_fourha_beta/h_123/gromacs"
dir2="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/H221F_fourha_beta/noh_123/gromacs"
GMVAE_labels=GMVAE_data[2*7501:]
KMean_labels=KMean_data[2*7501:]
GMVAE_ener_HF=calculate_ener(dir1,dir2,GMVAE_labels)
KMean_ener_HF=calculate_ener(dir1,dir2,GMVAE_labels)
print (GMVAE_ener_wt)
print (KMean_ener_wt)
print (GMVAE_ener_HF)
print (KMean_ener_HF)
