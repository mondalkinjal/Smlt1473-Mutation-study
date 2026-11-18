import numpy as np
import os
from itertools import islice
from scipy.stats import sem
import matplotlib.pyplot as plt
def format_values(values):
    if isinstance(values, list):
        return [f"{x:.3g}" for x in values]
    return f"{values:.3g}"
def format_percentage(percentage):
    return f"{percentage:.3g}%"
#os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs")
current_working_directory=os.getcwd()
GMVAE_data = np.load('labels_GMVAE.npy')
KMean_data = np.load('labels_kmeans.npy')
def calculate_ener(dir1,dir2,labels):
    #os.chdir(dir1)
    filename = "energy_protein_ligand.xvg"
    os.chdir(dir1)
#column1 = data[:, 0]
    print (os.getcwd())
#column2 = data[:, 1]
    with open(filename, 'r') as file:
        data = np.loadtxt(islice(file, 27, None))
    dataen1 = data[:, 1]
    dataen2 = data[:, 2]
    os.chdir(dir2)
    print (os.getcwd())
    with open(filename, 'r') as file:
        newdata = np.loadtxt(islice(file, 27, None))
    dataenr1 = newdata[:,1]
    dataenr2 = newdata[:,2]
    datax = np.concatenate((dataen1, dataenr1), axis=0)
    datay = np.concatenate((dataen2, dataenr2), axis=0)
    datat = datax + datay
    mean_total= np.average(datat)
    err_total= sem(datat)


    max_label=np.max(labels)
    avg=[]
    std=[]
    error=[]
    for i in range (0,5):

        positions = np.where(labels == i)
        value=np.average(datat[positions])
        stderror= sem(datat[positions])
        stdev=np.std(datat[positions])
        avg.append(value)
        std.append(stdev)
        error.append(stderror)
    return (avg,std,error,mean_total, err_total)
def replace_values (arr):
    return np.where(arr == 0, 3, np.where(arr == 1, 2, np.where(arr == 2, 4, np.where(arr == 3, 1, 0))))

KMean_data=replace_values(KMean_data)
dir1="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/hexamana/H109/gromacs"
dir2="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/hexamana/NOH109/gromacs"
GMVAE_labels=GMVAE_data[:2*7501]
KMean_labels=KMean_data[:2*7501]
GMVAE_ener_WT,GMVAE_std_WT,GMVAE_err_WT,GMVAEavgtotWT,GMVAEerrtotWT=calculate_ener(dir1,dir2,GMVAE_labels)
KMean_ener_WT,KMean_std_WT,KMean_err_WT,KMeanavgtotWT,KMeanerrtotWT=calculate_ener(dir1,dir2,KMean_labels)
dir1="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/H221F_hexamana/H109/gromacs"
dir2="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/H221F_hexamana/NOH109/gromacs"
GMVAE_labels=GMVAE_data[2*7501:4*7501]
KMean_labels=KMean_data[2*7501:4*7501]
GMVAE_ener_HF,GMVAE_std_HF,GMVAE_err_HF,GMVAEavgtotHF,GMVAEerrtotHF=calculate_ener(dir1,dir2,GMVAE_labels)
KMean_ener_HF,KMean_std_HF,KMean_err_HF,KMeanavgtotHF,KMeanerrtotHF=calculate_ener(dir1,dir2,KMean_labels)
dir1="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/R312L_hexamana/H109/gromacs"
dir2="/scratch/zt1/project/energybio/user/kinjal14/biochemistry_mutation/hexamana_mutation/R312L_hexamana/NOH109/gromacs"
GMVAE_labels=GMVAE_data[4*7501:6*7501]
KMean_labels=KMean_data[4*7501:6*7501]
GMVAE_ener_RL,GMVAE_std_RL,GMVAE_err_RL,GMVAEavgtotRL,GMVAEerrtotRL=calculate_ener(dir1,dir2,GMVAE_labels)
KMean_ener_RL,KMean_std_RL,KMean_err_RL,KMeanavgtotRL,KMeanerrtotRL=calculate_ener(dir1,dir2,KMean_labels)

print ("GMVAE-wt",format_values(GMVAE_ener_WT),format_values(GMVAE_err_WT),format_values(GMVAEavgtotWT),format_values(GMVAEerrtotWT))
print ("KMean-wt",format_values(KMean_ener_WT),format_values(KMean_err_WT),format_values(KMeanavgtotWT),format_values(KMeanerrtotWT))
print ("GMVAE-HF",format_values(GMVAE_ener_HF),format_values(GMVAE_err_HF),format_values(GMVAEavgtotHF),format_values(GMVAEerrtotHF))
print ("KMean-HF",format_values(KMean_ener_HF),format_values(KMean_err_HF),format_values(KMeanavgtotHF),format_values(KMeanerrtotHF))
print ("GMVAE-RL",format_values(GMVAE_ener_RL),format_values(GMVAE_err_RL),format_values(GMVAEavgtotRL),format_values(GMVAEerrtotRL))
print ("KMean-RL",format_values(KMean_ener_RL),format_values(KMean_err_RL),format_values(KMeanavgtotRL),format_values(KMeanerrtotRL))
os.chdir(current_working_directory)
x = np.arange(5)
bar_width = 0.12

# Positions for each bar group
positions_A = x - 2.5 * bar_width
positions_B = x - 1.5 * bar_width
positions_C = x - 0.5 * bar_width
positions_D = x + 0.5 * bar_width
positions_E = x + 1.5 * bar_width
positions_F = x + 2.5 * bar_width

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(positions_A, KMean_ener_WT, bar_width, label='KMean WT', yerr=KMean_err_WT, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.bar(positions_B, KMean_ener_HF, bar_width, label='KMean H221F', yerr=KMean_err_HF, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.bar(positions_C, KMean_ener_RL, bar_width, label='KMean R312L', yerr=KMean_err_RL, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.bar(positions_D, GMVAE_ener_WT, bar_width, label='GMVAE WT', yerr=GMVAE_err_WT, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.bar(positions_E, GMVAE_ener_HF, bar_width, label='GMVAE H221F', yerr=GMVAE_err_HF, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.bar(positions_F, GMVAE_ener_RL, bar_width, label='GMVAE R312L', yerr=GMVAE_err_RL, capsize=5, error_kw={'elinewidth': 1, 'ecolor': 'black'})
ax.set_xlabel('Cluster No', fontsize=12, fontweight='bold')
ax.set_ylabel('Interaction Energies (in KJ/mol) ', fontsize=12, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels([str(i) for i in x])
ax.legend()
ax.set_ylim(-200, -1000)
# Display the plot
plt.savefig('bar_plots.png')

GMVAE_data=GMVAE_data+1
KMean_data=KMean_data+1
GMVAE_labels=GMVAE_data[:2*7501]
KMean_labels=KMean_data[:2*7501]
total_elements = GMVAE_labels.size
GMVAE_counts = np.bincount(GMVAE_labels.flatten())
for i, count in enumerate(GMVAE_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s GMVAE WT: {count}  Percentage: {format_percentage(percentage)}%")

KMean_counts = np.bincount(KMean_labels.flatten())

# Total number of elements in the matrix
total_elements = KMean_labels.size

# Calculate and print the percentage of each number
for i, count in enumerate(KMean_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s KMean WT: {count}  Percentage: {format_percentage(percentage)}%")
GMVAE_labels=GMVAE_data[2*7501:4*7501]
KMean_labels=KMean_data[2*7501:4*7501]
total_elements = GMVAE_labels.size
GMVAE_counts = np.bincount(GMVAE_labels.flatten())
for i, count in enumerate(GMVAE_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s GMVAE H221F: {count}  Percentage: {format_percentage(percentage)}%")

KMean_counts = np.bincount(KMean_labels.flatten())

# Total number of elements in the matrix
total_elements = KMean_labels.size

# Calculate and print the percentage of each number
for i, count in enumerate(KMean_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s KMean H221F: {count}  Percentage: {format_percentage(percentage)}%")

GMVAE_labels=GMVAE_data[4*7501:6*7501]
KMean_labels=KMean_data[4*7501:6*7501]
total_elements = GMVAE_labels.size
GMVAE_counts = np.bincount(GMVAE_labels.flatten())
for i, count in enumerate(GMVAE_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s GMVAE R312L: {count}  Percentage: {format_percentage(percentage)}%")

KMean_counts = np.bincount(KMean_labels.flatten())

# Total number of elements in the matrix
total_elements = KMean_labels.size

# Calculate and print the percentage of each number
for i, count in enumerate(KMean_counts[1:], start=1):
    percentage = (count / total_elements) * 100
    print(f"Number of {i}'s KMean R312L: {count}  Percentage: {format_percentage(percentage)}%")
