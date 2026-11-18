import os
import numpy as np
directory_path ="/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation/fourha_beta/h_123/gromacs/saltbridges"
os.chdir(directory_path)
file_list = os.listdir()
threshold=3.5
fraction_threshold=0.20
l=[]
for file_name in file_list:
    
    end_name=file_name[-3:]
    if (end_name=='dat'):
        data=np.loadtxt(file_name)
        x_data = data[:, 0]  # First column (X)
        y_data = data[:, 1]  # Second column (Y)
        mask = data < threshold
        count = np.count_nonzero(mask)
        length=len(y_data)
        if ((count/length)>fraction_threshold):
            l.append(file_name)

        

print (l)
print (file_name[7:-4])
if isinstance(file_name, str):
    print("The variable is a string.")
    
