
import MDAnalysis as mda
import numpy as np
import pandas as pd
u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
final_array=np.zeros((12,len(u.trajectory)))
for i in range (0,len(u.trajectory)):
    u.trajectory[i]
    selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 201 or resid 204 or resid 291)")
    selection_2=u.select_atoms("resname BGLCN and resid 1")
    dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_2.center_of_mass(),box=[78.80383,78.80383,78.80383,90.,90.,90.])
    for j in range(0,12):
        final_array[j,i]=dist_arr[j,0]
x=[]
y=[]
z=[]
for i in range (1,13):
    for j in range (1,7502):
        y.append(i)
        x.append((j)/10.0)
        z.append(final_array[i-1,j-1])
import matplotlib.pyplot as plt
import matplotlib.colors
fig, axs=plt.subplots(figsize=(20,10))
bounds=[0,5,10,15,20,25,30]
colors=["red","yellow","green","pink","orange","blue"]
cmap = matplotlib.colors.ListedColormap(colors)
norm=matplotlib.colors.BoundaryNorm(bounds,len(colors))
sc = axs.scatter(x, y, c=z, cmap=cmap, norm=norm)
axs.set_yticks([1,2,3,4,5,6,7,8,9,10,11,12])
axs.set_yticklabels(['21','94','141','142','146','147','150','194','197','201','204','291'])
fig.colorbar(sc,spacing="proportional")
plt.xlabel('time',fontsize=20)
plt.ylabel('residue',fontsize=20)
plt.savefig("set1proteincontact.jpg")
plt.show()

