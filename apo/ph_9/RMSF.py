def rmsf(dir):
    os.chdir(dir)
    current_working_directory=os.getcwd()
    print (current_working_directory)

    result_1=np.zeros((2,308))
    u=mda.Universe("protein.gro","final_production.xtc")
    print ("yo")
    u.trajectory[0]
    average = align.AverageStructure(u, u, select='protein and name CA', ref_frame=0).run()
    print ("yo")
    ref = average.results.universe
    aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
    c_alphas = u.select_atoms('protein and name CA')
    R = rms.RMSF(c_alphas).run()
    x_axis=c_alphas.resids
    no_set=R.results.rmsf
    return (x_axis+21),no_set
#u=mda.Universe("protein_ligand.gro")
#    u.add_TopologyAttr('tempfactors')
#    protein = u.select_atoms('protein') # select protein atoms
#    for residue, r_value in zip(protein.residues, R.results.rmsf):
#        residue.atoms.tempfactors = r_value
#    protein = u.select_atoms('protein')

#    return protein
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
WTH109=current_working_directory+"/WT/H109/gromacs"
WTNOH109=current_working_directory+"/WT/NOH109/gromacs"
H221FH109=current_working_directory+"/H221F/H109/gromacs"
H221FNOH109=current_working_directory+"/H221F/NOH109/gromacs"
R312LH109=current_working_directory+"/R312L/H109/gromacs"
R312LNOH109=current_working_directory+"/R312L/NOH109/gromacs"
set_labels=["WT set1","WT set2","H221F set1","H221F set2","R312L set1","R312L set2"]
working_directories=[WTH109,WTNOH109,H221FH109,H221FNOH109,R312LH109,R312LNOH109]
dir_id=0

for i in range(0,3):
    for j in range(0,2):
        x_axis, y_axis=rmsf(working_directories[dir_id])
        os.chdir(current_working_directory)
        plt.plot(x_axis,y_axis,label=set_labels[dir_id])
#        print (current_working_directory, str(set_labels[dir_id])+str("protein.pdb"))
#        protein.write(str(set_labels[dir_id])+str("protein.pdb"))
        dir_id=dir_id+1

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
#os.chdir("/expanse/lustre/projects/mda123/kmondal/fresh_folder/fourha_mutation
