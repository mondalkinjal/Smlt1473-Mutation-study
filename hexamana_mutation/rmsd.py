import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
import os
#import pandas as pd
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
def rmsd_for_atomgroups(directory, selection1, selection2=None):
    """Calulate the RMSD for selected atom groups.

    Parameters
    ----------
    universe: MDAnalysis.core.universe.Universe
        MDAnalysis universe.
    selection1: str
        Selection string for main atom group, also used during alignment.
    selection2: list of str, optional
        Selection strings for additional atom groups.

    Returns
    -------
    rmsd_df: pandas.core.frame.DataFrame
        DataFrame containing RMSD of the selected atom groups over time.
    """
    os.chdir(directory)
    universe=mda.Universe("protein_ligand.gro","final_production.xtc")
    ref = universe.copy()  # Use first frame as reference
    aligner = align.AlignTraj(
        universe,
        ref,
        select=selection1,  # Align using the protein
        filename="aligned.xtc",  # Temporary file for aligned trajectory
        in_memory=True       # Keep trajectory in memory
    )
    aligner.run()

    ref = universe
    rmsd_analysis = rms.RMSD(universe, ref, select=selection1, groupselections=selection2)
    rmsd_analysis.run()
    final_rmsd = rmsd_analysis.results.rmsd.T   # transpose makes it easier for plotting
    #time = final_rmsd[1]
    #columns = [selection1, *selection2] if selection2 else [selection1]
    #rmsd_df = pd.DataFrame(np.round(rmsd_analysis.rmsd[:, 2:], 2), columns=columns)
    #rmsd_df.index.name = "frame"
    os.chdir(current_working_directory)
    return final_rmsd, universe
current_working_directory=os.getcwd()
WTH109=current_working_directory+"/hexamana/H109/gromacs"
WTNOH109=current_working_directory+"/hexamana/NOH109/gromacs"
H221FH109=current_working_directory+"/H221F_hexamana/H109/gromacs"
H221FNOH109=current_working_directory+"/H221F_hexamana/NOH109/gromacs"
R312LH109=current_working_directory+"/R312L_hexamana/H109/gromacs"
R312LNOH109=current_working_directory+"/R312L_hexamana/NOH109/gromacs"
set_labels=["A","B","C","D","E","F"]
working_directories=[WTH109,WTNOH109,H221FH109,H221FNOH109,R312LH109,R312LNOH109]

GMVAE_labels=np.load("labels_GMVAE.npy")

print (GMVAE_labels.shape)
#final_rmsd = rmsd_for_atomgroups(WTH123, "backbone", ["protein", "resname BGLCA or resname BGLCN"])
#import matplotlib.pyplot as plt
dir_id=0
fig,axs = plt.subplots(3,2,figsize=(10,8), sharex='all', sharey='all')
for i in range(0,3):
    for j in range(0,2):
        final_rmsd, universe = rmsd_for_atomgroups(working_directories[dir_id], "backbone", ["resid 15:41", "resname BMANA"])
        time=final_rmsd[1]/(1000)
        if (i==0 and j ==0):
            axs[i,j].plot(time, final_rmsd[2], 'k-',  label="backbone")
            axs[i,j].plot(time, final_rmsd[3], 'b-', label="residues 36-63")
            axs[i,j].text(50, 13.50, set_labels[dir_id], ha='center', va='center',fontweight='bold', fontsize=12)
#            axs[i,j].plot(time, final_rmsd[4], 'r-', label="sugar")
            axs[i,j].legend(loc="best")
        else:
            axs[i,j].plot(time, final_rmsd[2], 'k-')
            axs[i,j].plot(time, final_rmsd[3], 'b-')
            axs[i,j].text(50, 13.50, set_labels[dir_id], ha='center', va='center',fontweight='bold', fontsize=12)
#            axs[i,j].plot(time, final_rmsd[4], 'r-')
        axs[i,j].set_ylim(0, 15)
        dir_id=dir_id+1
fig.text(0.5, 0.04, "time(ns)", ha='center', va='center', fontweight='bold', fontsize=12)

# Set common y-axis label
fig.text(0.06, 0.5, r"RMSD ($\AA$)", ha='center', va='center', rotation='vertical', fontweight='bold', fontsize=12)
plt.subplots_adjust(wspace=0, hspace=0)
yticks = [ 2, 4, 6, 8, 10, 12, 14]
yticklabels = ['2.0', '4.0', '6.0', '8.0','10.0','12.0','14.0']
xticks = [100, 300, 500, 700]
xticklabels = ['100', '300', '500', '700'] 

for ax in axs.flat:
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
for ax in axs.flat:
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
os.chdir(current_working_directory)
plt.subplots_adjust(wspace=0, hspace=0)
plt.savefig("rmsd_protein.jpg")

dir_id=0

fig,axs = plt.subplots(3,2,figsize=(10,8), sharex='all', sharey='all')
for i in range(0,3):
    for j in range(0,2):
        final_rmsd, universe = rmsd_for_atomgroups(working_directories[dir_id], "backbone", ["resid 15:41", "resname BMANA"])
        time=final_rmsd[1]/(1000)
        if (i==0 and j ==0):
#            axs[i,j].plot(time, final_rmsd[2], 'k-',  label="backbone")
#            axs[i,j].plot(time, final_rmsd[3], 'b-', label="protein")
            axs[i,j].plot(time, final_rmsd[4], 'r-', label="sugar")
            axs[i,j].text(50, 19.00, set_labels[dir_id], ha='center', va='center',fontweight='bold',fontsize=12)
            axs[i,j].legend(loc="best")
            sugar_rmsd = final_rmsd[4]
            max_rmsd = np.max(sugar_rmsd)
            max_time = time[np.argmax(sugar_rmsd)]
            frame_idx = int(final_rmsd[0][np.argmax(sugar_rmsd)])
#            universe.trajectory[frame_idx]  # Go to the frame with max RMSD
            
#            print (GMVAE_labels.shape)
            GMVAE_curr_labels = GMVAE_labels[dir_id*7501:(dir_id+1)*7501] 
            GMVAE_true_label = GMVAE_curr_labels[frame_idx]
            print ("GMVAE_true_label",GMVAE_true_label)
#            final_rmsd[4][GMVAE_labels]
            positions = np.where(GMVAE_curr_labels == GMVAE_true_label)[0]
            rmsd_values = sugar_rmsd[positions]
            mean_rmsd = np.mean(rmsd_values)
            differences = np.abs(rmsd_values - mean_rmsd)
            min_idx_within_subset = np.argmin(differences)
            closest_position = positions[min_idx_within_subset]
            cluster_rmsd_values = sugar_rmsd[closest_position]
            print (f"Directory {dir_id}: cluster number for max_RMSD = {GMVAE_true_label} Å")
            print (f"Directory {dir_id}: most representative RMSD for cluster_RMSD = {cluster_rmsd_values:.2f} Å")
            universe.trajectory[closest_position]
            universe.atoms.write(f"max_rmsd_cluster_{set_labels[dir_id]}.pdb")
            print (f"Directory {dir_id}: Max sugar RMSD = {max_rmsd:.2f} Å at {max_time:.2f} ns")
            universe.trajectory[0]
            universe.atoms.write(f"initial_structure_{set_labels[dir_id]}.pdb")
            print(f"Directory {dir_id}: Max sugar RMSD = {max_rmsd:.2f} Å at {max_time:.2f} ns")
                            
        else:
#            axs[i,j].plot(time, final_rmsd[2], 'k-')
#            axs[i,j].plot(time, final_rmsd[3], 'b-')
            axs[i,j].plot(time, final_rmsd[4], 'r-')
            axs[i,j].text(50, 19.00, set_labels[dir_id], ha='center', va='center',fontweight='bold',fontsize=12)
            sugar_rmsd = final_rmsd[4]
            max_rmsd = np.max(sugar_rmsd)
            max_time = time[np.argmax(sugar_rmsd)]
            frame_idx = int(final_rmsd[0][np.argmax(sugar_rmsd)])
            universe.trajectory[frame_idx]  # Go to the frame with max RMSD
            
#            print ("GMVAE_true_label",GMVAE_true_label)
            GMVAE_curr_labels = GMVAE_labels[dir_id*7501:(dir_id+1)*7501]
            GMVAE_true_label = GMVAE_curr_labels[frame_idx]
            print ("GMVAE_true_label",GMVAE_true_label)
            positions = np.where(GMVAE_curr_labels == GMVAE_true_label)[0]
            rmsd_values = sugar_rmsd[positions]
            mean_rmsd = np.mean(rmsd_values)
            differences = np.abs(rmsd_values - mean_rmsd)
            min_idx_within_subset = np.argmin(differences)
            closest_position = positions[min_idx_within_subset]
            cluster_rmsd_values = sugar_rmsd[closest_position]
            print (f"Directory {dir_id}: cluster number for max_RMSD = {GMVAE_true_label}")
            print(f"Directory {dir_id}: most representative RMSD for cluster_RMSD = {cluster_rmsd_values:.2f} Å")
            universe.trajectory[closest_position]
            universe.atoms.write(f"max_rmsd_cluster_{set_labels[dir_id]}.pdb")
            print(f"Directory {dir_id}: Max sugar RMSD = {max_rmsd:.2f} Å at {max_time:.2f} ns")
            universe.trajectory[0]
            universe.atoms.write(f"initial_structure_{set_labels[dir_id]}.pdb")
            print(f"Directory {dir_id}: Max sugar RMSD = {max_rmsd:.2f} Å at {max_time:.2f} ns")
            
        axs[i,j].set_ylim(0, 20)
        dir_id=dir_id+1
fig.text(0.5, 0.04, "time(ns)", ha='center', va='center', fontweight='bold',fontsize=12)

# Set common y-axis label
fig.text(0.06, 0.5, r"RMSD ($\AA$)", ha='center', va='center', rotation='vertical', fontweight='bold',fontsize=12)
plt.subplots_adjust(wspace=0, hspace=0)
yticks = np.linspace(0, 20, 5)
yticklabels = ['0.0', '5.0', '10.0', '15.0', '20.0']
xticks = [100, 300, 500, 700]
xticklabels = ['100', '300', '500', '700']
for ax in axs.flat:
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)
for ax in axs.flat:
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
os.chdir(current_working_directory)
plt.subplots_adjust(wspace=0, hspace=0)

os.chdir(current_working_directory)
plt.savefig("rmsd_sugar.jpg")





