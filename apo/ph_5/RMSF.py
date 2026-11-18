def rmsf(dir):
    os.chdir(dir)

    result_1=np.zeros((2,308))
    u=mda.Universe("protein.gro","final_production.xtc")

    u.trajectory[0]
    average = align.AverageStructure(u, u, select='protein and name CA', ref_frame=0).run()
    ref = average.results.universe
    aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
    c_alphas = u.select_atoms('protein and name CA')
    R = rms.RMSF(c_alphas).run()
    x_axis=c_alphas.resids
    no_set=R.results.rmsf

#    u.add_TopologyAttr('tempfactors')
#    protein = u.select_atoms('protein') # select protein atoms
#    for residue, r_value in zip(protein.residues, R.results.rmsf):
#        residue.atoms.tempfactors = r_value
#    protein = u.select_atoms('protein')
#    return protein
    return (x_axis+21),no_set
    #current_working_directory=os.getcwd()
    #np.save("residue_no.npy",np.array(x_axis))
    #np.save("set1.npy",np.array(set1))
    #plt.plot(x_axis,set1)
    #plt.xlabel("residue_no")
    #plt.ylabel("rmsf")
    #plt.savefig("RMSF.jpg")
import MDAnalysis as mda
import numpy as np
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
import os
current_working_directory=os.getcwd()
WTH123=current_working_directory+"/WT/H123/gromacs"
WTNOH123=current_working_directory+"/WT/NOH123/gromacs"
H221FH123=current_working_directory+"/H221F/H123/gromacs"
H221FNOH123=current_working_directory+"/H221F/NOH123/gromacs"
set_labels=["A","B","C","D"]
working_directories=[WTH123,WTNOH123,H221FH123,H221FNOH123]
dir_id=0

for i in range(0,2):
    for j in range(0,2):
        x_axis,y_axis=rmsf(working_directories[dir_id])
#        protein=rmsf(working_directories[dir_id])
#        os.chdir(current_working_directory)
        plt.plot(x_axis,y_axis,label=set_labels[dir_id])
#        print (current_working_directory, str(set_labels[dir_id])+str("protein.pdb"))
#        protein.write(str(set_labels[dir_id])+str("protein.pdb"))
#        dir_id=dir_id+1
plt.xlabel("residue no",fontweight='bold')
plt.ylabel("RMSF",fontweight='bold')
plt.legend()
plt.savefig("RMSF.jpg")
# Plot the data and add labels
#ax.plot(xRL1, setRL1, label='RL_set1')
#ax.plot(xRL2, setRL2, label='RL_set2')

# Add a title and labels to the axes
#plt.ylim(0,3)
# Add a legend
#os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutatio
