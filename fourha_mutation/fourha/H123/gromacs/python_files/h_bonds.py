
import MDAnalysis
from MDAnalysis.analysis.hydrogenbonds.hbond_analysis import HydrogenBondAnalysis as HBA

u = MDAnalysis.Universe("protein_ligand.gro", "final_production.xtc")

hbond = HBA(universe=u)
hbond.hydrogens_sel = u.select_atoms("name H")
hbond.acceptors_sel = u.select_atoms("name C")
hbond.run()
res=HBA.results.hbonds
print (res.shape)
