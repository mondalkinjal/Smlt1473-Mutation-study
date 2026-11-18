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
#from backend_GMVAE.backend_GMVAE import GMVAE
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
    average_distance = avg_distance / len(u.trajectory)

    return average_distance

topology_file = 'protein_ligand.gro'
trajectory_file = 'final_production.xtc'
new_topology_file = 'protein_ligand.gro'
trajectory_file = 'final_production.xtc'
protein_selection = 'name CA and protein'  # Atom selection for the protein residues
ligand_selection = 'resname BGLCA or resname BGLCN'  # Atom selection for the ligand
current_working_directory=os.getcwd()
dH123=current_working_directory+"/H123"
nH123=7500
dNOH123=current_working_directory+"/NOH123"
nNOH123=7500
average_H123 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dH123,nH123)
average_NOH123 = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection,dNOH123,nNOH123)
matrices = [average_H123,
            average_NOH123]
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
def silly(k,combined_data):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(combined_data)
    label=kmeans.predict(combined_data)
    sc=silhouette_score(combined_data, label)
    print("Silhouette Score for {}:{}".format(k,sc))
    return sc
no=[]
score=[]
for j in range (2,18):
    sc=silly(j,combined_data)
    score.append(sc)
    no.append(j)

max_element=max(score)
max_index=score.index(max_element)
m_index=max_index+2
kmeans=KMeans(n_clusters=m_index)
clusters = kmeans.fit(combined_data)
os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation")
#kmeans=KMeans(n_clusters=4)
#clusters = kmeans.fit(combined_data)
np.save("cluster_KMeans.npy",clusters.labels_)
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
x=[]
for i in range (0,(ntetraha1+ntetraha2+nHFha1+nHFha2)):

    j=j+1
    x.append(i)
# Plot in the first subplot
axs[0].plot(x[0:(ntetraha1+ntetraha2)], clusters.labels_[0:(ntetraha1+ntetraha2)])
axs[0].set_title('tetraha')
axs[0].legend()

# Plot in the second subplot
axs[1].plot(x[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)], clusters.labels_[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)])
axs[1].set_title('H221F')
axs[1].legend()

# Plot in the third subplot


# Add space between subplots
plt.tight_layout()

# Add a main title to the entire figure
#plt.suptitle('K-Means')

# Show the plot
#In this example, we use plt.subplots to create a 1x3 grid of subplots within a single figure. We then plot different functions in each subplot using the individual axs objects. The figsize parameter in the plt.subplots function determines the size of the entire figure. The plt.tight_layout() function is used to add spacing between the subplots, and plt.suptitle() adds a main title to the entire figure.
plt.savefig("K-Means.jpg")
#plt.show()





    

