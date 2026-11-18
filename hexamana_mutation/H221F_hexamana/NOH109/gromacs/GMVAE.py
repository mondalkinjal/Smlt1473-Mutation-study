
#import py3Dmol
import MDAnalysis as mda
import numpy as np
#import pandas as pd
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
u=mda.Universe("protein_ligand.gro","final_production.xtc")
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


def calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection):
    # Load the topology and trajectory files
    u = mda.Universe(topology_file, trajectory_file)

    # Select the protein residues and ligand atoms
    protein_residues = u.select_atoms(protein_selection)
    ligand_atoms = u.select_atoms(ligand_selection)

    # Create an empty list to store the distances
    num_residues=len(protein_residues)
    avg_distance=np.zeros(num_residues)

    # Iterate over all frames in the trajectory
    for ts in u.trajectory:
        # Calculate distances between protein residues and ligand atoms
        dist = distances.distance_array(protein_residues.positions, ligand_atoms.positions)

        # Average the distances for each residue
        avg_dist_per_residue = dist.mean(axis=1)

        # Add the average distances to the overall list
        avg_distance=np.add(avg_distance,avg_dist_per_residue)

    # Calculate the overall average distance
    average_distance = avg_distance / len(u.trajectory)

    return average_distance
def silly(k,combined_data):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(combined_data)
    label=kmeans.predict(combined_data)
    sc=silhouette_score(combined_data, label)
    print("Silhouette Score for {}:{}".format(k,sc))
    return sc

topology_file = 'protein_ligand.gro'
trajectory_file = 'final_production.xtc'
protein_selection = 'name CA and protein'  # Atom selection for the protein residues
ligand_selection = 'resname BGLCA or resname BGLCN'  # Atom selection for the ligand

average_distance = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection)

def standardize_columns(matrix):
    matrix_max = np.max(matrix, axis=0)
    matrix_min = np.min(matrix, axis=0)
    standardized_matrix = (matrix - mean) / std
    return standardized_matrix



def find_elements_less_than(arr, threshold):
    indices = np.where(arr < threshold)[0]
    elements = arr[indices]
    return indices, elements

# Example usage
threshold_value = 15
indices, elements = find_elements_less_than(average_distance, threshold_value)
print("Indices:", indices)
print("Elements:", elements)

selection = u.select_atoms(f"name CA and resid {' '.join(map(str, indices))}")
selection_1=u.select_atoms("resname BGLCN and resid 1")
selection_2=u.select_atoms("resname BGLCA and resid 2")
selection_3=u.select_atoms("resname BGLCN and resid 3")
selection_4=u.select_atoms("resname BGLCA and resid 4")
data=[]
print ("yes")
for ts in u.trajectory:
        # Calculate distances between protein residues and ligand atoms
    dist_1 = distances.distance_array(selection.positions, selection_1.positions)
    dist_2 = distances.distance_array(selection.positions, selection_2.positions)
    dist_3 = distances.distance_array(selection.positions, selection_3.positions)
    dist_4 = distances.distance_array(selection.positions, selection_4.positions)
    avg_dist_per_residue_1 = dist_1.mean(axis=1)
    avg_dist_per_residue_2 = dist_2.mean(axis=1)
    avg_dist_per_residue_3 = dist_3.mean(axis=1)
    avg_dist_per_residue_4 = dist_4.mean(axis=1)
    final_array=np.concatenate((avg_dist_per_residue_1, avg_dist_per_residue_2, avg_dist_per_residue_3, avg_dist_per_residue_4))
    data.append(final_array)
combined_data=np.stack(data,axis=0)
print ("yes")
print(combined_data.shape)


def standardize_columns(matrix):
    mean = np.max(matrix, axis=0)
    std = np.min(matrix, axis=0)
    standardized_matrix = (matrix - std) / (mean-std)
    return standardized_matrix

# Example usage
combined_data = standardize_columns(combined_data)
#print (combined_data[0,:])
#print (combined_data[1000,:])
#print (combined_data[2000,:])
#print (combined_data[3000,:])
#print (combined_data[4000,:])
#print (combined_data[5000,:])
#print (combined_data[6000,:])
#print (combined_data[7000,:])
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
parser.add_argument('--learning_rate', default=1e-3, type=float, help='learning rate (default: 0.001)')
parser.add_argument('--decay_epoch', default=-1, type=int, help='Reduces the learning rate every decay_epoch')
parser.add_argument('--lr_decay', default=0.5, type=float, help='Learning rate decay for training (default: 0.5)')

## Architecture
parser.add_argument('--num_classes', type=int, default=4, help='number of classes (default: 10)')
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

## Others
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
print (labels_test)
np.save("labels_test.npy",labels_test)
