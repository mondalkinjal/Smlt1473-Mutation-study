import MDAnalysis as mda
import numpy as np
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.gridspec as gridspec
def fluctuations_for_atomgroups(directory):
    os.chdir(directory)
    u=mda.Universe("protein_ligand.gro","final_production.xtc")
    x=[]
    for i in range (0,7501):
        u.trajectory[i]
        selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 200 or resid 204 or resid 291)")
        dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_1.positions)
        x.append(dist_arr)
    dist_numpy=np.stack(x,axis=2)
    std_array=np.std(dist_numpy,axis=2)
    return std_array
current_working_directory=os.getcwd()
WTH109=current_working_directory+"/hexamana/H109/gromacs"
WTNOH109=current_working_directory+"/hexamana/NOH109/gromacs"
H221FH109=current_working_directory+"/H221F_hexamana/H109/gromacs"
H221FNOH109=current_working_directory+"/H221F_hexamana/NOH109/gromacs"
R312LH109=current_working_directory+"/R312L_hexamana/H109/gromacs"
R312LNOH109=current_working_directory+"/R312L_hexamana/NOH109/gromacs"
set_labels=["A","B","C","D","E","F"]
working_directories=[WTH109,WTNOH109,H221FH109,H221FNOH109,R312LH109,R312LNOH109]
min_value=0
max_value=6
x=[]
dir_id=0
plt.rcParams.update({'font.size': 18})
fig,axs = plt.subplots(3,2,figsize=(18,20))
start = -5
end = 15
num_bins = 12

# Calculate bin width
bin_width = (end - start) / num_bins

# Calculate bin centers
bin_centers = [start + (bin_width / 2) + (i * bin_width) for i in range(num_bins)]
#gs1 = gridspec.GridSpec(10, 10)
#gs1.update(wspace=0.025, hspace=0.05) # set the spacing between axes.
for i in range(0,3):
    for j in range(0,2):
        std_array= fluctuations_for_atomgroups(working_directories[dir_id])
        im = axs[i,j].imshow(std_array, cmap='gray',origin='upper',vmin=min_value,vmax=max_value, aspect='auto', extent=[-5, 15, 11.5, -0.5])
        axs[i,j].set_yticks([0,1,2,3,4,5,6,7,8,9,10,11])
        axs[i,j].set_yticklabels(['42','115','162','163','167','168','171','215','218','221','225','312'])
        axs[i,j].set_ylabel('residue no',fontweight='bold')
        axs[i,j].set_xlabel('residue no',fontweight='bold')
        axs[i,j].set_xticks(bin_centers)

        axs[i,j].set_xticklabels(['42','115','162','163','167','168','171','215','218','221','225','312'])
        axs[i,j].tick_params(axis='x')
        axs[i,j].tick_params(axis='y')
        axs[i,j].set_title(set_labels[dir_id],fontweight='bold')
        dir_id=dir_id+1
plt.subplots_adjust(right=0.85)

cbar_ax = fig.add_axes([0.91, 0.15, 0.03, 0.7])
cbar=fig.colorbar(im, cax=cbar_ax, orientation='vertical', shrink=0.8)
#cbar.ax.tick_params(labelsize=13)
#ani = animation.FuncAnimation(fig, animate, frames=len(u.trajectory), interval=70)
cbar.set_label(r"fluctuations of distance ($\AA$)",fontsize=18,fontweight='bold')

os.chdir(current_working_directory)

plt.savefig("time_fluctuations.jpg")
plt.show()
