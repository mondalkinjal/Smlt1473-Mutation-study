silly_cutoff=0.4
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
GMVAE_labels=np.load("labels_GMVAE.npy")
KMeans_labels=np.load("labels_KMeans.npy")
print (GMVAE_labels.shape)
RMSD_values=np.load("final_rmsd.npy")
max_label=np.max(GMVAE_labels)
score=[]
GMVAElabels_set1=GMVAE_labels[0:7501]
#GMVAElabels_set2=GMVAE_labels[7501:

#for i in range (0,max_label+1):
#    positions = np.where(labels == i)
#    RMSD_values[positions
