
import MDAnalysis as mda
import numpy as np
import pandas as pd
import os
current_working_directory=os.getcwd()
print (current_working_directory)
#os.chdir('/home/kinjal/klauda_project/set2_tetraha')
#current_working_directory=os.getcwd()
#print (current_working_directory)
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
import matplotlib.pyplot as plt
result_1=np.zeros((2,308))
u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
u.trajectory[0]
average = align.AverageStructure(u, u, select='protein and name CA',
                                 ref_frame=0).run()
ref = average.results.universe
aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
c_alphas = u.select_atoms('protein and name CA')
R = rms.RMSF(c_alphas).run()
x_axis=c_alphas.resids
set1=R.results.rmsf
current_working_directory=os.getcwd()
np.save("residue_no.npy",np.array(x_axis))
np.save("set1.npy",np.array(set1))

#os.chdir('/home/kinjal/klauda_project/set2_tetraha')
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
#u.trajectory[0]
#average = align.AverageStructure(u, u, select='protein and name CA',
#                                 ref_frame=0).run()
#ref = average.results.universe
#aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
#c_alphas = u.select_atoms('protein and name CA')
#R = rms.RMSF(c_alphas).run()
#set2=R.results.rmsf
#current_working_directory=os.getcwd()
#print (current_working_directory)

#os.chdir('/home/kinjal/klauda_project/set3_tetraha')
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
#u.trajectory[0]
#average = align.AverageStructure(u, u, select='protein and name CA',
#                                 ref_frame=0).run()
#ref = average.results.universe
#aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
#c_alphas = u.select_atoms('protein and name CA')
#R = rms.RMSF(c_alphas).run()
#set3=R.results.rmsf
#current_working_directory=os.getcwd()
#print (current_working_directory)

#os.chdir('/home/kinjal/klauda_project/set4_tetraha')
#u=mda.Universe("step4.1_equilibration.gro","final_production.xtc")
#u.trajectory[0]
#average = align.AverageStructure(u, u, select='protein and name CA',
#                                 ref_frame=0).run()
#ref = average.results.universe
#aligner = align.AlignTraj(u, ref,select='protein and name CA',in_memory=True).run()
#c_alphas = u.select_atoms('protein and name CA')
#R = rms.RMSF(c_alphas).run()
#set4=R.results.rmsf
#current_working_directory=os.getcwd()
#print (current_working_directory)

#fig = plt.figure(figsize=(4,4))
#ax = fig.add_subplot(111)
#ax.plot(x_axis, set1, 'k-',  label="set1")
#ax.plot(x_axis, set2, 'b-', label="set2")
#ax.plot(x_axis, set3, 'r-', label="set3")
#ax.plot(x_axis, set4, 'c-', label="set4")

#ax.legend(loc="best")
#ax.set_xlabel("residue_no")
#ax.set_ylabel("RMSF ($\AA$)")
#fig.savefig("rmsf.jpg")
