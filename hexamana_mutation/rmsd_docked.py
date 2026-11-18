import MDAnalysis as mda
from MDAnalysis.analysis import align, rms
import os

# Define directory and paths
struct_dir = "/home/kinjal14/scratch.energybio/biochemistry_mutation/hexamana_mutation"  # Replace with your directory
ref_path = os.path.join(struct_dir, "hexamana/H109/gromacs/step3_input.gro")
mobile_path_H221F = os.path.join(struct_dir, "H221F_hexamana/H109/gromacs/step3_input.gro")
mobile_path_R312L = os.path.join(struct_dir, "R312L_hexamana/H109/gromacs/step3_input.gro")
# Load universes
ref = mda.Universe(ref_path)
mobile_H221F = mda.Universe(mobile_path_H221F)
mobile_R312L = mda.Universe(mobile_path_R312L)
# Align entire protein
alignment_H221F=align.alignto(mobile_H221F, ref, select="protein")
alignment_R312L=align.alignto(mobile_R312L, ref, select="protein")

protein_rmsd_H221F = alignment_H221F[1]  # RMSD after alignment
protein_rmsd_R312L = alignment_R312L[1]
print(f"Protein RMSD H221F (post-alignment): {protein_rmsd_H221F:.3f} Å")
print(f"Protein RMSD R312L (post-alignment): {protein_rmsd_R312L:.3f} Å")

# Compute RMSD of sugar ligand (adjust resname)
ref_sugar = ref.select_atoms("resname BMANA")
mobile_sugar_H221F = mobile_H221F.select_atoms("resname BMANA")
mobile_sugar_R312L = mobile_R312L.select_atoms("resname BMANA")
sugar_rmsd_H221F = rms.rmsd(mobile_sugar_H221F.positions, ref_sugar.positions, superposition=False)
sugar_rmsd_R312L = rms.rmsd(mobile_sugar_R312L.positions, ref_sugar.positions, superposition=False)

print(f"Sugar RMSD H221F: {sugar_rmsd_H221F:.3f} Å")
print(f"Sugar RMSD R312L: {sugar_rmsd_R312L:.3f} Å")
