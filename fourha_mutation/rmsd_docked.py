import MDAnalysis as mda
from MDAnalysis.analysis import align, rms
import os

# Define directory and paths
struct_dir = "/home/kinjal14/scratch.energybio/biochemistry_mutation/fourha_mutation"  # Replace with your directory
ref_path = os.path.join(struct_dir, "fourha/H123/gromacs/step3_input.gro")
mobile_path = os.path.join(struct_dir, "H221F_fourha/H123/gromacs/step3_input.gro")

# Load universes
ref = mda.Universe(ref_path)
mobile = mda.Universe(mobile_path)

# Align entire protein
alignment=align.alignto(mobile, ref, select="protein")
protein_rmsd = alignment[1]  # RMSD after alignment
print(f"Protein RMSD (post-alignment): {protein_rmsd:.3f} Å")

# Compute RMSD of sugar ligand (adjust resname)
ref_sugar = ref.select_atoms("resname BGLCA or resname BGLCN")
mobile_sugar = mobile.select_atoms("resname BGLCA or resname BGLCN")
sugar_rmsd = rms.rmsd(mobile_sugar.positions, ref_sugar.positions, superposition=False)

print(f"Sugar RMSD: {sugar_rmsd:.3f} Å")
