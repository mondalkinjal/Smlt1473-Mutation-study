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
ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10,11])
ax.set_yticklabels(['42','115','162','163','167','168','171','215','218','222','225','312'])
ax.set_ylabel('residue no')
ax.set_xlabel('residue no')
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11])
ax.set_xticklabels(['42','115','162','163','167','168','171','215','218','222','225','312'])
min_value=0
max_value=6
x=[]
for i in range (0,7501):
    u.trajectory[i]
    selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 201 or resid 204 or resid 291)")
    dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_1.positions)
    x.append(dist_arr)
dist_numpy=np.stack(x,axis=2)
std_array=np.std(dist_numpy,axis=2)
im = ax.imshow(std_array, cmap='gray',origin='upper',vmin=min_value,vmax=max_value)
fig.colorbar(im,cax=cax).ax.set_ylabel('Distance (Angstrom)')
#ani = animation.FuncAnimation(fig, animate, frames=len(u.trajectory), interval=70)
plt.savefig("time_fluctuations.jpg")
plt.show()
