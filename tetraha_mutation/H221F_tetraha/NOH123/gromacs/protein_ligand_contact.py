import MDAnalysis as mda
import numpy as np
#import pandas as pd
u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
final_array=np.zeros((12,len(u.trajectory)))
for i in range (0,len(u.trajectory)):
    u.trajectory[i]
    selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 201 or resid 291)")
    print (selection_1.positions)
    selection_2=u.select_atoms("resname BGLCN or resname BGLCA")
    #print (selection_2.center_of_mass())
    dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_2.positions,box=[78.80383,78.80383,78.80383,90.,90.,90.])
    #print (dist_arr)
    #print ("yes")
    #print (dist_arr.shape)
    for j in range(0,11):
        final_array[j,i]=dist_arr[j,0]
x=[]
y=[]
z=[]
for i in range (1,12):
    for j in range (1,7502):
        y.append(i)
        x.append((j)/10.0)
        z.append(final_array[i-1,j-1])
np.save("protein_ligand_contact.npy",final_array)
import matplotlib.pyplot as plt
import matplotlib.colors
fig, axs=plt.subplots(figsize=(20,10))
bounds=[0,11,22,33,44,55,66]
colors=["red","yellow","green","pink","orange","blue"]
cmap = matplotlib.colors.ListedColormap(colors)
norm=matplotlib.colors.BoundaryNorm(bounds,len(colors))
sc = axs.scatter(x, y, c=z, cmap=cmap, norm=norm)
axs.set_yticks([1,2,3,4,5,6,7,8,9,10,11])
axs.set_yticklabels(['42','115','162','163','167','168','171','215','218','222','312'])
fig.colorbar(sc,spacing="proportional")
plt.xlabel('time',fontsize=20)
plt.ylabel('residue',fontsize=20)
plt.savefig("protein_ligand_contact.jpg")
