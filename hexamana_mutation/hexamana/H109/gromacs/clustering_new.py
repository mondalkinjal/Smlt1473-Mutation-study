
import py3Dmol
import MDAnalysis as mda
import numpy as np
import pandas as pd
u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
import MDAnalysis as mda
from MDAnalysis.analysis import distances
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
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







# Example usage
topology_file = 'step4.1_equilibration.gro'
trajectory_file = 'final_production.xtc'
protein_selection = 'name CA and protein'  # Atom selection for the protein residues
ligand_selection = 'resname BGLCA or resname BGLCN'  # Atom selection for the ligand
def silly(k,combined_data):
    kmeans=KMeans(n_clusters=k)
    kmeans.fit(combined_data)
    label=kmeans.predict(combined_data)
    sc=silhouette_score(combined_data, label)
    print("Silhouette Score for {}:{}".format(k,sc))
    return sc







# Example usage
topology_file = 'step4.1_equilibration.gro'
trajectory_file = 'final_production.xtc'
protein_selection = 'name CA and protein'  # Atom selection for the protein residues
ligand_selection = 'resname BGLCA or resname BGLCN'  # Atom selection for the ligand

average_distance = calculate_average_distance(topology_file, trajectory_file, protein_selection, ligand_selection)

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
no=[]
score=[]
for j in range (2,20):
    sc=silly(j,combined_data)
    score.append(sc)
    no.append(j)

max_element=max(score)
max_index=score.index(max_element)
m_index=max_index+2
kmeans=KMeans(n_clusters=m_index)
clusters = kmeans.fit(combined_data)
x=[]
for i in range (0,len(u.trajectory)):

    j=j+1
    x.append(i)

plt.plot(x,clusters.labels_)

plt.savefig("cluster_plot.jpg")

plt.show()

































