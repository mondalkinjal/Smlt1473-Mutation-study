import MDAnalysis as mda
import numpy as np
u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable
fig, ax=plt.subplots()
div = make_axes_locatable(ax)
cax = div.append_axes('right', '5%', '5%')
ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_yticklabels(['21','94','141','142','146','147','150','194','197','201','204'])
ax.set_ylabel('residue no')
ax.set_xlabel('residue no')
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels(['21','94','141','142','146','147','150','194','197','201','204'])
min_value=0
max_value=6
x=[]
for i in range (0,7501):
    u.trajectory[i]
    selection_1=u.select_atoms("name CA and (resid 42 or resid 115 or resid 162 or resid 163 or resid 167 or resid 168 or resid 171 or resid 215 or resid 218 or resid 222 or resid 225)")
    dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_1.positions)
    x.append(dist_arr)
dist_numpy=np.stack(x,axis=2)
std_array=np.std(dist_numpy,axis=2)
im = ax.imshow(std_array, cmap='gray',origin='upper',vmin=min_value,vmax=max_value)
fig.colorbar(im,cax=cax).ax.set_ylabel('Distance (Angstrom)')
#ani = animation.FuncAnimation(fig, animate, frames=len(u.trajectory), interval=70)
plt.savefig("time_fluctuations.jpg")
plt.show()
