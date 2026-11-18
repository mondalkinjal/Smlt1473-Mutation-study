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
KMeans=np.load("labels_kmeans.npy")
GMVAE=np.load("labels_GMVAE.npy")
fig,axs = plt.subplots(2,2,figsize=(10,8))
nfourha1=7501
nfourha2=7501
nHFha1=7501
nHFha2=7501
time = np.arange(0, (nfourha1+nfourha2))
def replace_values (arr):
    return np.where(arr ==0, 1, np.where(arr == 1, 2, np.where(arr == 2, 0, 3)))
# Divide the array by 10
GMVAE=replace_values(GMVAE)
time = time / 10
axs[0,0].plot(time,KMeans[0:(nfourha1+nfourha2)],marker='o', linestyle='') 
axs[0,0].set_xlabel("time (ns)",fontweight='bold')
axs[0,0].set_xticks([0,150,300,450,600,750,900,1050,1200,1350,1500])
axs[0,0].set_xticklabels(['0','150','300','450','600','750','150','300','450','600','750'])
axs[0,0].set_ylabel("cluster no",fontweight='bold')
axs[0,0].set_yticks([0,1,2,3])
axs[0,0].set_yticklabels(['0','1','2','3'])
axs[0,0].set_title("A",fontweight='bold')
axs[0,0].axvline(x=750, color='red', linestyle='--')

axs[0,1].plot(time,KMeans[(nfourha1+nfourha2):(nfourha1+nfourha2+nHFha1+nHFha2)],marker='o', linestyle='')
axs[0,1].set_xlabel("time (ns)",fontweight='bold')
axs[0,1].set_xticks([0,150,300,450,600,750,900,1050,1200,1350,1500])
axs[0,1].set_xticklabels(['0','150','300','450','600','750','150','300','450','600','750'])
axs[0,1].set_ylabel("cluster no",fontweight='bold')
axs[0,1].set_yticks([0,1,2,3])
axs[0,1].set_yticklabels(['0','1','2','3'])
axs[0,1].set_title("B",fontweight='bold')
axs[0,1].axvline(x=750, color='red', linestyle='--')

axs[1,0].plot(time,GMVAE[0:(nfourha1+nfourha2)],marker='o', linestyle='')
axs[1,0].set_xlabel("time (ns)",fontweight='bold')
axs[1,0].set_xticks([0,150,300,450,600,750,900,1050,1200,1350,1500])
axs[1,0].set_xticklabels(['0','150','300','450','600','750','150','300','450','600','750'])
axs[1,0].set_ylabel("cluster no",fontweight='bold')
axs[1,0].set_yticks([0,1,2,3])
axs[1,0].set_yticklabels(['0','1','2','3'])
axs[1,0].set_title("C",fontweight='bold')
axs[1,0].axvline(x=750, color='red', linestyle='--')

axs[1,1].plot(time,GMVAE[(nfourha1+nfourha2):(nfourha1+nfourha2+nHFha1+nHFha2)],marker='o', linestyle='')
axs[1,1].set_xlabel("time (ns)",fontweight='bold')
axs[1,1].set_xticks([0,150,300,450,600,750,900,1050,1200,1350,1500])
axs[1,1].set_xticklabels(['0','150','300','450','600','750','150','300','450','600','750'])
axs[1,1].set_ylabel("cluster no",fontweight='bold')
axs[1,1].set_yticks([0,1,2,3])
axs[1,1].set_yticklabels(['0','1','2','3'])
axs[1,1].set_title("D",fontweight='bold')
axs[1,1].axvline(x=750, color='red', linestyle='--')

plt.subplots_adjust(hspace=0.5)
plt.savefig("clusters.jpg")

