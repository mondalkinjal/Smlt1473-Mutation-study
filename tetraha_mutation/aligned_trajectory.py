import MDAnalysis as mda
import numpy as np
import os
#import pandas as pd
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
from MDAnalysis.coordinates.XTC import XTCWriter
current_working_directory=os.getcwd()
dH123=current_working_directory+"/H123/gromacs"
dNOH123=current_working_directory+"/NOH123/gromacs"
os.chdir(dH123)
u=mda.Universe("protein_ligand.gro","final_production.xtc")
ref_structure = mda.Universe('protein_ligand.gro')
align.AlignTraj(u, ref_structure,select='all', filename='aligned.xtc',in_memory=True).run()

all_atoms = u.select_atoms("all")
all_atoms.write('aligned.xtc', frames='all')
# Save the aligned trajectory
os.chdir(dNOH123)
u=mda.Universe("protein_ligand.gro","final_production.xtc")
ref_structure = mda.Universe('protein_ligand.gro')
align.AlignTraj(u, ref_structure,select='all', filename='aligned.xtc',in_memory=True).run()

all_atoms = u.select_atoms("all")
all_atoms.write('aligned.xtc', frames='all')
# Save the aligned trajectory

