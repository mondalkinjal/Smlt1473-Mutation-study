import MDAnalysis as mda
import numpy as np
#import pandas as pd
u=mda.Universe("protein_ligand.gro","final_production.xtc")
from MDAnalysis.analysis import rms, diffusionmap, align
from MDAnalysis.analysis.distances import dist
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA
def rmsd_for_atomgroups(universe, selection1, selection2=None):
    """Calulate the RMSD for selected atom groups.

    Parameters
    ----------
    universe: MDAnalysis.core.universe.Universe
        MDAnalysis universe.
    selection1: str
        Selection string for main atom group, also used during alignment.
    selection2: list of str, optional
        Selection strings for additional atom groups.

    Returns
    -------
    rmsd_df: pandas.core.frame.DataFrame
        DataFrame containing RMSD of the selected atom groups over time.
    """

    universe.trajectory[0]
    ref = universe
    rmsd_analysis = rms.RMSD(universe, ref, select=selection1, groupselections=selection2)
    rmsd_analysis.run()
    final_rmsd = rmsd_analysis.results.rmsd.T   # transpose makes it easier for plotting
    #time = final_rmsd[1]
    #columns = [selection1, *selection2] if selection2 else [selection1]
    #rmsd_df = pd.DataFrame(np.round(rmsd_analysis.rmsd[:, 2:], 2), columns=columns)
    #rmsd_df.index.name = "frame"
    return final_rmsd
final_rmsd = rmsd_for_atomgroups(u, "backbone", ["protein", "resname BMANA"])
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4,4))
time=final_rmsd[1]
time=time/(1000)
ax = fig.add_subplot(111)
ax.plot(time, final_rmsd[2], 'k-',  label="backbone")
ax.plot(time, final_rmsd[3], 'b-', label="protein")
ax.plot(time, final_rmsd[4], 'r-', label="sugar")
np.save("final_rmsd.npy",final_rmsd[4])
ax.legend(loc="best")
ax.set_xlabel("time (ns)")
ax.set_ylabel(r"RMSD ($\AA$)")
fig.savefig("rmsd.jpg")
