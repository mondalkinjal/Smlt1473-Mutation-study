import MDAnalysis as mda
import numpy as np
#import pandas as pd
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
import matplotlib.colors
import os
def colorbar(directory):
    os.chdir(directory)
    u=mda.Universe("protein_ligand.gro","final_production.xtc")
    final_array=np.zeros((12,len(u.trajectory)))
    for i in range (0,len(u.trajectory)):
        u.trajectory[i]
        selection_1=u.select_atoms("name CA and (resid 21 or resid 94 or resid 141 or resid 142 or resid 146 or resid 147 or resid 150 or resid 194 or resid 197 or resid 200 or resid 204 or resid 291)")
        #print (selection_1.positions)
        selection_2=u.select_atoms("resname BMANA")
        #print (selection_2.center_of_mass())
        dist_arr = mda.analysis.distances.distance_array(selection_1.positions,selection_2.positions,box=[78.80383,78.80383,78.80383,90.,90.,90.])
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
    os.chdir(current_working_directory)
    return x,y,z
current_working_directory=os.getcwd()
WTH109=current_working_directory+"/hexamana/H109/gromacs"
WTNOH109=current_working_directory+"/hexamana/NOH109/gromacs"
H221FH109=current_working_directory+"/H221F_hexamana/H109/gromacs"
H221FNOH109=current_working_directory+"/H221F_hexamana/NOH109/gromacs"
R312LH109=current_working_directory+"/R312L_hexamana/H109/gromacs"
R312LNOH109=current_working_directory+"/R312L_hexamana/NOH109/gromacs"
set_labels=["A","B","C","D","E","F"]
working_directories=[WTH109,WTNOH109,H221FH109,H221FNOH109,R312LH109,R312LNOH109]
fig,axs = plt.subplots(3,2,figsize=(10,8))
bounds=[0,11,22,33,44,55,66]
colors=["red","yellow","green","pink","orange","blue"]
cmap = matplotlib.colors.ListedColormap(colors)
norm=matplotlib.colors.BoundaryNorm(bounds,len(colors))
dir_id=0
for i in range(0,3):
    print (i)
    for j in range(0,2):
        x,y,z=colorbar(working_directories[dir_id])
        sc = axs[i,j].scatter(x, y, c=z, cmap=cmap, norm=norm)
        axs[i,j].set_yticks([1,2,3,4,5,6,7,8,9,10,11,12])
        axs[i,j].set_yticklabels(['42','115','162','163','167','168','171','215','218','221','225','312'])
        axs[i,j].set_xlabel("time (ns)",fontweight='bold')
        axs[i,j].set_ylabel("residue",fontweight='bold')
        axs[i,j].set_title(set_labels[dir_id],fontweight='bold')
        dir_id=dir_id+1
cbar_ax = fig.add_axes([0.91, 0.15, 0.03, 0.7])
cbar=fig.colorbar(sc,cax=cbar_ax, orientation='vertical', shrink=0.8)
#cbar.ax.tick_params(labelsize=20)
cbar.set_label(r"distance ($\AA$)",fontsize=13,fontweight='bold')
#np.save("protein_ligand_contact.npy",final_array)
#plt.xlabel('time(ns)',fontsize=20)
#plt.ylabel('residue',fontsize=20)
#plt.yticks(fontsize=20)
#plt.xticks(fontsize=20)
plt.subplots_adjust(hspace=0.5)
plt.savefig("protein_ligand_contact.jpg")
