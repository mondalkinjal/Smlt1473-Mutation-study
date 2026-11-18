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
def fluctuations_for_atomgroups(directory):
    os.chdir(directory)
    u=mda.Universe("protein_ligand.gro","final_production.xtc")
    x=[]
    for i in range (0,7501):
        u.trajectory[i]
        selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 201 or resid 204)")
        dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_1.positions)
        x.append(dist_arr)
    dist_numpy=np.stack(x,axis=2)
    std_array=np.std(dist_numpy,axis=2)
    return std_array
current_working_directory=os.getcwd()
WTH123=current_working_directory+"/tetraha/H123/gromacs"
WTNOH123=current_working_directory+"/tetraha/NOH123/gromacs"
H221FH123=current_working_directory+"/H221F_tetraha/H123/gromacs"
H221FNOH123=current_working_directory+"/H221F_tetraha/NOH123/gromacs"
set_labels=["A","B","C","D"]
working_directories=[WTH123,WTNOH123,H221FH123,H221FNOH123]
min_value=0
max_value=6
x=[]
dir_id=0
fig,axs = plt.subplots(2,2,figsize=(16,10))
for i in range(0,2):
    for j in range(0,2):
        std_array= fluctuations_for_atomgroups(working_directories[dir_id])
        im = axs[i,j].imshow(std_array, cmap='gray',origin='upper',vmin=min_value,vmax=max_value,aspect='auto', extent=[-0.5, 11.5, 11.5, -0.5])
        axs[i,j].set_yticks([0,1,2,3,4,5,6,7,8,9,10,11])
        axs[i,j].set_yticklabels(['42','115','162','163','167','168','171','215','218','221','225','312'])
        axs[i,j].set_ylabel('residue no',fontweight='bold')
        axs[i,j].set_xlabel('residue no',fontweight='bold')
        axs[i,j].set_xticks([0,1,2,3,4,5,6,7,8,9,10,11])
        axs[i,j].set_xticklabels(['42','115','162','163','167','168','171','215','218','221','225','312'])
        axs[i,j].tick_params(axis='x')
        axs[i,j].tick_params(axis='y')
        axs[i,j].set_title(set_labels[dir_id],fontweight='bold')
        dir_id=dir_id+1
cbar_ax = fig.add_axes([0.91, 0.15, 0.03, 0.7])
cbar=fig.colorbar(im, cax=cbar_ax, orientation='vertical', shrink=0.8)
#cbar.ax.tick_params(labelsize=13)
#ani = animation.FuncAnimation(fig, animate, frames=len(u.trajectory), interval=70)
cbar.set_label(r"fluctuations of distance ($\AA$)",fontsize=13,fontweight='bold')
#plt.subplots_adjust(hspace=0.5)
#fig.tight_layout()
os.chdir(current_working_directory)

plt.savefig("time_fluctuations.jpg")
plt.show()
