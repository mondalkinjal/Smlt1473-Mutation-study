import numpy as np
import matplotlib.pyplot as plt
GMVAE_data = np.load('labels_GMVAE.npy')
KMean_data = np.load('labels_kmeans.npy')
GMVAE_data=GMVAE_data+1
KMean_data=KMean_data+1
total_elements = GMVAE_data.size
GMVAE_counts = np.bincount(GMVAE_data.flatten())

# Total number of elements in the matrix
#total_elements = matrix.size
def replace_values (arr):
    return np.where(arr == 0, 7, np.where(arr == 1, 2, np.where(arr == 2, 10, np.where(arr == 3, 5, np.where(arr == 4, 4, np.where(arr == 5, 6 , np.where(arr == 6, 3, np.where(arr == 7, 0, np.where(arr == 11, 1, np.where(arr == 8, 11, np.where(arr == 9, 8, 9)))))))))))

# Calculate and print the percentage of each number
for i, count in enumerate(GMVAE_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s GMVAE: {count}  Percentage: {percentage:.2f}%")
KMean_counts = np.bincount(KMean_data.flatten())

# Total number of elements in the matrix
total_elements = KMean_data.size

# Calculate and print the percentage of each number
for i, count in enumerate(KMean_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s KMean: {count}  Percentage: {percentage:.2f}%")
ntetraha1=7500
#dtetraha2="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/tetraha/correct_set/no_h_123/gromacs"
ntetraha2=7500
#dHFha1="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/H221F_tetraha/correct_set/h_123/gromacs"
nHFha1=7500
#dHFha2="/expanse/lustre/projects/mda123/kmondal/fresh_folder/tetraha_mutation/H221F_tetraha/correct_set/no_h_123/gromacs"
nHFha2=7500
KMean_data=KMean_data-1
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
x=[]
for i in range (0,(ntetraha1+ntetraha2+nHFha1+nHFha2)):

#    j=j+1
    x.append(i)
# Plot in the first subplot
axs[0].plot(x[0:(ntetraha1+ntetraha2)], KMean_data[0:(ntetraha1+ntetraha2)])
axs[0].set_title('tetraha', fontsize=20)
axs[0].legend()
axs[0].set_yticks([0,1,2,3])
axs[0].set_yticklabels(['0','1','2','3'])
axs[0].set_xticks([0,2500,5000,7500,10000,12500,15000])
axs[0].set_xticklabels(['0','250','500','750','1000', '1250', '1500'])
axs[0].set_xlabel('time(ns)',fontsize=20)
axs[0].set_ylabel('cluster',fontsize=20)

# Plot in the second subplot
axs[1].plot(x[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)], KMean_data[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)])
axs[1].set_title('H221F', fontsize=20)
axs[1].legend()
axs[1].set_yticks([0,1,2,3])
axs[1].set_yticklabels(['0','1','2','3'])
axs[1].set_xticks([15000,17500,20000,22500,25000,27500,30000])
axs[1].set_xticklabels(['0','250','500','750','1000', '1250', '1500'])
axs[1].set_xlabel('time(ns)',fontsize=20)
axs[1].set_ylabel('cluster',fontsize=20)

# Plot in the third subplot
for ax in axs:
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)

# Add space between subplots
plt.tight_layout()
plt.savefig("KMeans.jpg")
GMVAE_data=GMVAE_data-1
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
x=[]
for i in range (0,(ntetraha1+ntetraha2+nHFha1+nHFha2)):

#    j=j+1
    x.append(i)
# Plot in the first subplot
axs[0].plot(x[0:(ntetraha1+ntetraha2)], GMVAE_data[0:(ntetraha1+ntetraha2)])
axs[0].set_title('tetraha', fontsize=20)
axs[0].legend()
axs[0].set_yticks([0,1,2,3])
axs[0].set_yticklabels(['0','1','2','3'])
axs[0].set_xticks([0,2500,5000,7500,10000,12500,15000])
axs[0].set_xticklabels(['0','250','500','750','1000', '1250', '1500'])
axs[0].set_xlabel('time(ns)',fontsize=20)
axs[0].set_ylabel('cluster',fontsize=20)

# Plot in the second subplot
axs[1].plot(x[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)], GMVAE_data[(ntetraha1+ntetraha2):(ntetraha1+ntetraha2+nHFha1+nHFha2)])
axs[1].set_title('H221F', fontsize=20)
axs[1].legend()
axs[1].set_yticks([0,1,2,3])
axs[1].set_yticklabels(['0','1','2','3'])
axs[1].set_xticks([15000,17500,20000,22500,25000,27500,30000])
axs[1].set_xticklabels(['0','250','500','750','1000', '1250', '1500'])
axs[1].set_xlabel('time(ns)',fontsize=20)
axs[1].set_ylabel('cluster',fontsize=20)

# Plot in the third subplot
for ax in axs:
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)

# Add space between subplots
plt.tight_layout()
plt.savefig("GMVAE.jpg")
