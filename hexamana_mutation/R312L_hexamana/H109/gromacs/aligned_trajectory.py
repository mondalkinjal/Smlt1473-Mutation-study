import MDAnalysis as mda
import numpy as np
import os
#import pandas as pd
#u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
from MDAnalysis.coordinates.XTC import XTCWriter
print (os.getcwd())
u=mda.Universe("protein_ligand.gro","final_production.xtc")
ref_structure = mda.Universe('protein_ligand.gro')
align.AlignTraj(u, ref_structure,select='all', filename='aligned.xtc',in_memory=True).run()

all_atoms = u.select_atoms("all")
all_atoms.write('aligned.xtc', frames='all')

# Save the aligned trajectory

