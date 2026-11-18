import MDAnalysis as mda
import numpy as np
#import pandas as pd
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
#from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
import MDAnalysis as mda
from MDAnalysis.analysis import distances
#from sklearn.cluster import KMeans
#from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
#from torchvision import datasets, t:wransforms
from torch.utils.data.sampler import SubsetRandomSampler
import torch.utils.data
from scipy.io import loadmat
from backend_GMVAE.backend_GMVAE import GMVAE
import matplotlib.pyplot as plt
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dr,num):
    # Load the topology and trajectory files
    os.chdir(dr)
    current_working_directory=os.getcwd()
    u = mda.Universe(topology_file, trajectory_file)

    # Select the protein residues and ligand atoms
    protein_residues = u.select_atoms(protein_selection)
    ligand_atoms = u.select_atoms(ligand_selection)

    # Create an empty list to store the distances
    num_residues=len(protein_residues)
    avg_distance=np.zeros(num_residues)
    v=0
    # Iterate over all frames in the trajectory
    for ts in u.trajectory:
        # Calculate distances between protein residues and ligand atoms
        dist = distances.distance_array(protein_residues.positions, ligand_atoms.positions, box=[78.80383,78.80383,78.80383,90.,90.,90.])

        # Average the distances for each residue
        avg_dist_per_residue = dist.mean(axis=1)

        # Add the average distances to the overall list
        avg_distance=np.add(avg_distance,avg_dist_per_residue)
        v=v+1
        if v>num:
            break
    # Calculate the overall average distance
    average_distance = avg_distance

    return average_distance

topology_file = 'protein_ligand.gro'
trajectory_file = 'final_production.xtc'
new_topology_file = 'protein_ligand.gro'
trajectory_file = 'final_production.xtc'
protein_selection = 'name CA and protein'  # Atom selection for the protein residues
ligand_selection = 'resname BGLCA or resname BGLCN'  # Atom selection for the ligand
dtetraha1="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/tetraha_mutation/tetraha/H123/gromacs"
ntetraha1=7500
dtetraha2="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/tetraha_mutation/tetraha/NOH123/gromacs"
ntetraha2=7500
dHFha1="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/tetraha_mutation/H221F_tetraha/H123/gromacs"
nHFha1=7500
dHFha2="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/tetraha_mutation/H221F_tetraha/NOH123/gromacs"
nHFha2=7500
average_tetraha1 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dtetraha1,ntetraha1)
average_tetraha2 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dtetraha2,ntetraha2)
average_HF1 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dHFha1,nHFha1)
average_HF2 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dHFha2,nHFha2)
matrices = [average_tetraha1,
            average_tetraha2,
            average_HF1,
            average_HF2]
#matrices=[average_MMMM2]
# Initialize the result matrix
result = np.zeros_like(matrices[0])

# Add the matrices
for matrix in matrices:
    result = np.add(result, matrix)
#result=result/nMMMM2
result=result/(ntetraha1+ntetraha2+nHFha1+nHFha2)
def standardize_columns(matrix):
    print ("yeah")
    mean = np.max(matrix, axis=0)
    std = np.min(matrix, axis=0)
    standardized_matrix = (matrix - std) / (mean-std)
    print ("yeah")
    return standardized_matrix



def find_elements_less_than(arr, threshold):
    indices = np.where(arr < threshold)[0]
    elements = arr[indices]
    return indices, elements

# Example usage
threshold_value = 25
print (result)
indices, elements = find_elements_less_than(result, threshold_value)
print("Indices:", indices)
print("Elements:", elements)

sel = f"name CA and resid {' '.join(map(str, indices))}"
BGLCN_1="resname BGLCN and resid 1"
BGLCA_2="resname BGLCA and resid 2"
BGLCN_3="resname BGLCN and resid 3"
BGLCA_4="resname BGLCA and resid 4"
structure="protein_ligand.gro"
trajectory="final_production.xtc"
data=[]
#print ("yes")
def combined_func(selection,selection_1, selection_2, selection_3, selection_4, structure, trajectory, dr, num,data):
    os.chdir(dr)
    current_working_directory=os.getcwd()
    u = mda.Universe(topology_file, trajectory_file)
    selection=u.select_atoms(selection)
    selection_1=u.select_atoms(selection_1)
    selection_2=u.select_atoms(selection_2)
    selection_3=u.select_atoms(selection_3)
    selection_4=u.select_atoms(selection_4)
    v=0
    for ts in u.trajectory:
        # Calculate distances between protein residues and ligand atoms
        dist_1 = distances.distance_array(selection.positions, selection_1.positions, box=[78.80383,78.80383,78.80383,90.,90.,90.])
        dist_2 = distances.distance_array(selection.positions, selection_2.positions, box=[78.80383,78.80383,78.80383,90.,90.,90.])
        dist_3 = distances.distance_array(selection.positions, selection_3.positions, box=[78.80383,78.80383,78.80383,90.,90.,90.])
        dist_4 = distances.distance_array(selection.positions, selection_4.positions, box=[78.80383,78.80383,78.80383,90.,90.,90.])
        avg_dist_per_residue_1 = dist_1.mean(axis=1)
        avg_dist_per_residue_2 = dist_2.mean(axis=1)
        avg_dist_per_residue_3 = dist_3.mean(axis=1)
        avg_dist_per_residue_4 = dist_4.mean(axis=1)
        final_array=np.concatenate((avg_dist_per_residue_1, avg_dist_per_residue_2, avg_dist_per_residue_3, avg_dist_per_residue_4 ))
        data.append(final_array)
        v=v+1
        if (v>num):
            break
    return data
data=combined_func(sel,BGLCN_1,BGLCA_2,BGLCN_3,BGLCA_4,structure,trajectory,dtetraha1,ntetraha1,data)
data=combined_func(sel,BGLCN_1,BGLCA_2,BGLCN_3,BGLCA_4,structure,trajectory,dtetraha2,ntetraha2,data)
data=combined_func(sel,BGLCN_1,BGLCA_2,BGLCN_3,BGLCA_4,structure,trajectory,dHFha1,nHFha1,data)
data=combined_func(sel,BGLCN_1,BGLCA_2,BGLCN_3,BGLCA_4,structure,trajectory,dHFha2,nHFha2,data)
combined_data=np.stack(data,axis=0)
print ("yes")
print(combined_data.shape)
combined_data = standardize_columns(combined_data)
parser = argparse.ArgumentParser(description='PyTorch Implementation of DGM Clustering')
## Used only in notebooks
parser.add_argument('-f', '--file', help='Path for input file. First line should contain number of lines to search in')

## Dataset
parser.add_argument('--seed', type=int, default=1, help='random seed (default: 1)')

## GPU
parser.add_argument('--cuda', type=int, default=1, help='use of cuda (default: 1)')
parser.add_argument('--gpuID', type=int, default=0, help='set gpu id to use (default: 0)')

## Training
parser.add_argument('--epochs', type=int, default=100, help='number of total epochs to run (default: 200)')
parser.add_argument('--batch_size', default=64, type=int, help='mini-batch size (default: 64)')
parser.add_argument('--batch_size_val', default=200, type=int, help='mini-batch size of validation (default: 200)')
parser.add_argument('--learning_rate', default=1e-4, type=float, help='learning rate (default: 0.001)')
parser.add_argument('--decay_epoch', default=-1, type=int, help='Reduces the learning rate every decay_epoch')
parser.add_argument('--lr_decay', default=0.5, type=float, help='Learning rate decay for training (default: 0.5)')

## Architecture
parser.add_argument('--num_classes', type=int, default=12, help='number of classes (default: 10)')
parser.add_argument('--gaussian_size', default=64, type=int, help='gaussian size (default: 64)')
parser.add_argument('--input_size', default=combined_data.shape[1], type=int, help='input size (default: 784)')
parser.add_argument('--train_proportion', default=1.0, type=float, help='proportion of examples to consider for training only (default: 1.0)')


## Gumbel parameters
parser.add_argument('--init_temp', default=1.0, type=float, help='Initial temperature used in gumbel-softmax (recommended 0.5-1.0, default:1.0)')
parser.add_argument('--decay_temp', default=1, type=int, help='Set 1 to decay gumbel temperature at every epoch (default: 1)')
parser.add_argument('--hard_gumbel', default=0, type=int, help='Set 1 to use the hard version of gumbel-softmax (default: 1)')
parser.add_argument('--min_temp', default=0.5, type=float, help='Minimum temperature of gumbel-softmax after annealing (default: 0.5)' )
parser.add_argument('--decay_temp_rate', default=0.013862944, type=float, help='Temperature decay rate at every epoch (default: 0.013862944)')

## Loss function parameters
parser.add_argument('--w_gauss', default=2, type=float, help='weight of gaussian loss (default: 1)')
parser.add_argument('--w_categ', default=1, type=float, help='weight of categorical loss (default: 1)')
parser.add_argument('--w_rec', default=1, type=float, help='weight of reconstruction loss (default: 1)')
parser.add_argument('--rec_type', type=str, choices=['bce', 'mse'],default='bce', help='desired reconstruction loss function (default: bce)')
#combined_data=(combined_data - np.min(combined_data)) / (np.max(combined_data)-np.min(combined_data))
parser.add_argument('--verbose', default=1, type=int, help='print extra information at every epoch.(default: 0)')

args = parser.parse_args()
## Random Seed
SEED = args.seed
np.random.seed(SEED)
random.seed(SEED)
torch.manual_seed(SEED)
if args.cuda:
  torch.cuda.manual_seed(SEED)
def partition_dataset(n, proportion=0.8):
  train_num = int(n * proportion)
  indices = np.random.permutation(n)
  train_indices, val_indices = indices[:train_num], indices[train_num:]
  return train_indices, val_indices
train_dataset=combined_data
test_dataset=combined_data
if args.train_proportion == 1.0:
  # we use all train dataset without partitioning
  train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)
  test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=args.batch_size_val, shuffle=False)
  val_loader = test_loader
else:
  # partition dataset according to train_proportion
  train_indices, val_indices = partition_dataset(len(train_dataset), args.train_proportion)
  # create data loaders for train, validation and test datasets
  train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size, sampler=SubsetRandomSampler(train_indices))
  val_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size_val, sampler=SubsetRandomSampler(val_indices))
  test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=args.batch_size_val, shuffle=False)
gmvae = GMVAE(args)
history_loss = gmvae.train(train_loader,val_loader)
test_loss,recon_test,gauss_test,cat_test, labels_test=gmvae.test(test_loader)
#np.save("clustering_GMVAE.npy",labels_test)

import os
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation")
np.save("clustering_GMVAE.npy",labels_test)
#kmeans=KMeans(n_clusters=4)ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
#clusters = kmeans.fit(combined_data
#labels_test=np.load("labels_test.npy")
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
x=[]
j=0
for i in range (0,(ntetraha1+ntetraha2+ntetraha1+ntetraha2)):

    j=j+1
    x.append(i)
# Plot in the first subplot
axs[0].plot(x[0:(ntetraha1+ntetraha2)], labels_test[0:(ntetraha1+ntetraha2)])
axs[0].set_title('tetraha')
axs[0].legend()

# Plot in the second subplot
axs[1].plot(x[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)], labels_test[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)])
axs[1].set_title('H221F')
axs[1].legend()

# Plot in the third subplot

# Add space between subplots
plt.tight_layout()

# Add a main title to the entire figure
#plt.suptitle('K-Means')

# Show the plot
#In this example, we use plt.subplots to create a 1x3 grid of subplots within a single figure. We then plot different functions in each subplot using the individual axs objects. The figsize parameter in the plt.subplots function determines the size of the entire figure. The plt.tight_layout() function is used to add spacing between the subplots, and plt.suptitle() adds a main title to the entire figure.
plt.savefig("GMVAE.jpg")
