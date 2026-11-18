# Complete source index

Inventory checked on 2026-11-18. This index lists all **770 original research code and configuration files** in the MD release. All 770 match the archived `biochemistry_mutation` files byte for byte. The GitHub baseline also contains the original README (771 files total).

See the [analysis guide](ANALYSIS_GUIDE.md) for the workflow, [docking reference](DOCKING.md) for Rosetta tutorials and recovery status, and [code audit](CODE_AUDIT.md) for static-check limitations. This inventory does not establish a file-to-figure mapping.

| File type | Count |
|---|---:|
| Notebook (`.ipynb`) | 49 |
| GROMACS parameters (`.mdp`) | 167 |
| Python (`.py`) | 335 |
| Slurm script (`.sb`) | 112 |
| Shell script (`.sh`) | 37 |
| Tcl/VMD (`.tcl`) | 19 |
| YAML configuration/environment (`.yml`) | 51 |

Duplicate filenames and historical variants are retained in their original system directories.

## (root) (7 files)

| File | Type |
|---|---|
| [GNN.yml](../GNN.yml) | YAML configuration/environment |
| [aligned_total.sb](../aligned_total.sb) | Slurm script |
| [aligned_trajectory.py](../aligned_trajectory.py) | Python |
| [aligned_trajectory.sb](../aligned_trajectory.sb) | Slurm script |
| [clustering_rmsd.sb](../clustering_rmsd.sb) | Slurm script |
| [read_extract_pka.py](../read_extract_pka.py) | Python |
| [reduced.sb](../reduced.sb) | Slurm script |

## apo (107 files)

| File | Type |
|---|---|
| [apo/ph_5/H221F/H123/addCrystPdb.py](../apo/ph_5/H221F/H123/addCrystPdb.py) | Python |
| [apo/ph_5/H221F/H123/checkfft.py](../apo/ph_5/H221F/H123/checkfft.py) | Python |
| [apo/ph_5/H221F/H123/glycan.yml](../apo/ph_5/H221F/H123/glycan.yml) | YAML configuration/environment |
| [apo/ph_5/H221F/H123/gromacs/mdout.mdp](../apo/ph_5/H221F/H123/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/H123/gromacs/prodrun.sh](../apo/ph_5/H221F/H123/gromacs/prodrun.sh) | Shell script |
| [apo/ph_5/H221F/H123/gromacs/reduced.sh](../apo/ph_5/H221F/H123/gromacs/reduced.sh) | Shell script |
| [apo/ph_5/H221F/H123/gromacs/run.sh](../apo/ph_5/H221F/H123/gromacs/run.sh) | Shell script |
| [apo/ph_5/H221F/H123/gromacs/step4.0_minimization.mdp](../apo/ph_5/H221F/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/H123/gromacs/step4.1_equilibration.mdp](../apo/ph_5/H221F/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/H123/gromacs/step5_production.mdp](../apo/ph_5/H221F/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/NOH123/addCrystPdb.py](../apo/ph_5/H221F/NOH123/addCrystPdb.py) | Python |
| [apo/ph_5/H221F/NOH123/checkfft.py](../apo/ph_5/H221F/NOH123/checkfft.py) | Python |
| [apo/ph_5/H221F/NOH123/glycan.yml](../apo/ph_5/H221F/NOH123/glycan.yml) | YAML configuration/environment |
| [apo/ph_5/H221F/NOH123/gromacs/mdout.mdp](../apo/ph_5/H221F/NOH123/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/NOH123/gromacs/prodrun.sh](../apo/ph_5/H221F/NOH123/gromacs/prodrun.sh) | Shell script |
| [apo/ph_5/H221F/NOH123/gromacs/reduced.sh](../apo/ph_5/H221F/NOH123/gromacs/reduced.sh) | Shell script |
| [apo/ph_5/H221F/NOH123/gromacs/run.sh](../apo/ph_5/H221F/NOH123/gromacs/run.sh) | Shell script |
| [apo/ph_5/H221F/NOH123/gromacs/step4.0_minimization.mdp](../apo/ph_5/H221F/NOH123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/NOH123/gromacs/step4.1_equilibration.mdp](../apo/ph_5/H221F/NOH123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_5/H221F/NOH123/gromacs/step5_production.mdp](../apo/ph_5/H221F/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_5/RMSF.py](../apo/ph_5/RMSF.py) | Python |
| [apo/ph_5/WT/H123/addCrystPdb.py](../apo/ph_5/WT/H123/addCrystPdb.py) | Python |
| [apo/ph_5/WT/H123/checkfft.py](../apo/ph_5/WT/H123/checkfft.py) | Python |
| [apo/ph_5/WT/H123/glycan.yml](../apo/ph_5/WT/H123/glycan.yml) | YAML configuration/environment |
| [apo/ph_5/WT/H123/gromacs/mdout.mdp](../apo/ph_5/WT/H123/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_5/WT/H123/gromacs/prodrun.sh](../apo/ph_5/WT/H123/gromacs/prodrun.sh) | Shell script |
| [apo/ph_5/WT/H123/gromacs/reduced.sh](../apo/ph_5/WT/H123/gromacs/reduced.sh) | Shell script |
| [apo/ph_5/WT/H123/gromacs/run.sh](../apo/ph_5/WT/H123/gromacs/run.sh) | Shell script |
| [apo/ph_5/WT/H123/gromacs/step4.0_minimization.mdp](../apo/ph_5/WT/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_5/WT/H123/gromacs/step4.1_equilibration.mdp](../apo/ph_5/WT/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_5/WT/H123/gromacs/step5_production.mdp](../apo/ph_5/WT/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_5/WT/NOH123/addCrystPdb.py](../apo/ph_5/WT/NOH123/addCrystPdb.py) | Python |
| [apo/ph_5/WT/NOH123/checkfft.py](../apo/ph_5/WT/NOH123/checkfft.py) | Python |
| [apo/ph_5/WT/NOH123/glycan.yml](../apo/ph_5/WT/NOH123/glycan.yml) | YAML configuration/environment |
| [apo/ph_5/WT/NOH123/gromacs/mdout.mdp](../apo/ph_5/WT/NOH123/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_5/WT/NOH123/gromacs/prodrun.sh](../apo/ph_5/WT/NOH123/gromacs/prodrun.sh) | Shell script |
| [apo/ph_5/WT/NOH123/gromacs/reduced.sh](../apo/ph_5/WT/NOH123/gromacs/reduced.sh) | Shell script |
| [apo/ph_5/WT/NOH123/gromacs/run.sh](../apo/ph_5/WT/NOH123/gromacs/run.sh) | Shell script |
| [apo/ph_5/WT/NOH123/gromacs/step4.0_minimization.mdp](../apo/ph_5/WT/NOH123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_5/WT/NOH123/gromacs/step4.1_equilibration.mdp](../apo/ph_5/WT/NOH123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_5/WT/NOH123/gromacs/step5_production.mdp](../apo/ph_5/WT/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_5/fluctuations.py](../apo/ph_5/fluctuations.py) | Python |
| [apo/ph_5/rmsd.py](../apo/ph_5/rmsd.py) | Python |
| [apo/ph_9/H221F/H109/addCrystPdb.py](../apo/ph_9/H221F/H109/addCrystPdb.py) | Python |
| [apo/ph_9/H221F/H109/checkfft.py](../apo/ph_9/H221F/H109/checkfft.py) | Python |
| [apo/ph_9/H221F/H109/glycan.yml](../apo/ph_9/H221F/H109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/H221F/H109/gromacs/mdout.mdp](../apo/ph_9/H221F/H109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/H109/gromacs/prodrun.sh](../apo/ph_9/H221F/H109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/H221F/H109/gromacs/reduced.sh](../apo/ph_9/H221F/H109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/H221F/H109/gromacs/run.sh](../apo/ph_9/H221F/H109/gromacs/run.sh) | Shell script |
| [apo/ph_9/H221F/H109/gromacs/step4.0_minimization.mdp](../apo/ph_9/H221F/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/H109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/H221F/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/H109/gromacs/step5_production.mdp](../apo/ph_9/H221F/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/NOH109/addCrystPdb.py](../apo/ph_9/H221F/NOH109/addCrystPdb.py) | Python |
| [apo/ph_9/H221F/NOH109/checkfft.py](../apo/ph_9/H221F/NOH109/checkfft.py) | Python |
| [apo/ph_9/H221F/NOH109/glycan.yml](../apo/ph_9/H221F/NOH109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/H221F/NOH109/gromacs/mdout.mdp](../apo/ph_9/H221F/NOH109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/NOH109/gromacs/prodrun.sh](../apo/ph_9/H221F/NOH109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/H221F/NOH109/gromacs/reduced.sh](../apo/ph_9/H221F/NOH109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/H221F/NOH109/gromacs/run.sh](../apo/ph_9/H221F/NOH109/gromacs/run.sh) | Shell script |
| [apo/ph_9/H221F/NOH109/gromacs/step4.0_minimization.mdp](../apo/ph_9/H221F/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/NOH109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/H221F/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/H221F/NOH109/gromacs/step5_production.mdp](../apo/ph_9/H221F/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/H109/addCrystPdb.py](../apo/ph_9/R312L/H109/addCrystPdb.py) | Python |
| [apo/ph_9/R312L/H109/checkfft.py](../apo/ph_9/R312L/H109/checkfft.py) | Python |
| [apo/ph_9/R312L/H109/glycan.yml](../apo/ph_9/R312L/H109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/R312L/H109/gromacs/mdout.mdp](../apo/ph_9/R312L/H109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/H109/gromacs/prodrun.sh](../apo/ph_9/R312L/H109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/R312L/H109/gromacs/reduced.sh](../apo/ph_9/R312L/H109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/R312L/H109/gromacs/run.sh](../apo/ph_9/R312L/H109/gromacs/run.sh) | Shell script |
| [apo/ph_9/R312L/H109/gromacs/step4.0_minimization.mdp](../apo/ph_9/R312L/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/H109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/R312L/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/H109/gromacs/step5_production.mdp](../apo/ph_9/R312L/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/NOH109/addCrystPdb.py](../apo/ph_9/R312L/NOH109/addCrystPdb.py) | Python |
| [apo/ph_9/R312L/NOH109/checkfft.py](../apo/ph_9/R312L/NOH109/checkfft.py) | Python |
| [apo/ph_9/R312L/NOH109/glycan.yml](../apo/ph_9/R312L/NOH109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/R312L/NOH109/gromacs/mdout.mdp](../apo/ph_9/R312L/NOH109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/NOH109/gromacs/prodrun.sh](../apo/ph_9/R312L/NOH109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/R312L/NOH109/gromacs/reduced.sh](../apo/ph_9/R312L/NOH109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/R312L/NOH109/gromacs/run.sh](../apo/ph_9/R312L/NOH109/gromacs/run.sh) | Shell script |
| [apo/ph_9/R312L/NOH109/gromacs/step4.0_minimization.mdp](../apo/ph_9/R312L/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/NOH109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/R312L/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/R312L/NOH109/gromacs/step5_production.mdp](../apo/ph_9/R312L/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/RMSF.py](../apo/ph_9/RMSF.py) | Python |
| [apo/ph_9/WT/H109/addCrystPdb.py](../apo/ph_9/WT/H109/addCrystPdb.py) | Python |
| [apo/ph_9/WT/H109/checkfft.py](../apo/ph_9/WT/H109/checkfft.py) | Python |
| [apo/ph_9/WT/H109/glycan.yml](../apo/ph_9/WT/H109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/WT/H109/gromacs/mdout.mdp](../apo/ph_9/WT/H109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/WT/H109/gromacs/prodrun.sh](../apo/ph_9/WT/H109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/WT/H109/gromacs/reduced.sh](../apo/ph_9/WT/H109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/WT/H109/gromacs/run.sh](../apo/ph_9/WT/H109/gromacs/run.sh) | Shell script |
| [apo/ph_9/WT/H109/gromacs/step4.0_minimization.mdp](../apo/ph_9/WT/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/WT/H109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/WT/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/WT/H109/gromacs/step5_production.mdp](../apo/ph_9/WT/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/WT/NOH109/addCrystPdb.py](../apo/ph_9/WT/NOH109/addCrystPdb.py) | Python |
| [apo/ph_9/WT/NOH109/checkfft.py](../apo/ph_9/WT/NOH109/checkfft.py) | Python |
| [apo/ph_9/WT/NOH109/glycan.yml](../apo/ph_9/WT/NOH109/glycan.yml) | YAML configuration/environment |
| [apo/ph_9/WT/NOH109/gromacs/mdout.mdp](../apo/ph_9/WT/NOH109/gromacs/mdout.mdp) | GROMACS parameters |
| [apo/ph_9/WT/NOH109/gromacs/prodrun.sh](../apo/ph_9/WT/NOH109/gromacs/prodrun.sh) | Shell script |
| [apo/ph_9/WT/NOH109/gromacs/reduced.sh](../apo/ph_9/WT/NOH109/gromacs/reduced.sh) | Shell script |
| [apo/ph_9/WT/NOH109/gromacs/run.sh](../apo/ph_9/WT/NOH109/gromacs/run.sh) | Shell script |
| [apo/ph_9/WT/NOH109/gromacs/step4.0_minimization.mdp](../apo/ph_9/WT/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [apo/ph_9/WT/NOH109/gromacs/step4.1_equilibration.mdp](../apo/ph_9/WT/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [apo/ph_9/WT/NOH109/gromacs/step5_production.mdp](../apo/ph_9/WT/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [apo/ph_9/fluctuations.py](../apo/ph_9/fluctuations.py) | Python |
| [apo/ph_9/rmsd.py](../apo/ph_9/rmsd.py) | Python |
| [apo/read_extract_pka.py](../apo/read_extract_pka.py) | Python |

## tetraha_mutation (149 files)

| File | Type |
|---|---|
| [tetraha_mutation/H221F_tetraha/H123/addCrystPdb.py](../tetraha_mutation/H221F_tetraha/H123/addCrystPdb.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/checkfft.py](../tetraha_mutation/H221F_tetraha/H123/checkfft.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/glycan.yml](../tetraha_mutation/H221F_tetraha/H123/glycan.yml) | YAML configuration/environment |
| [tetraha_mutation/H221F_tetraha/H123/glycan_mod.yml](../tetraha_mutation/H221F_tetraha/H123/glycan_mod.yml) | YAML configuration/environment |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/GMVAE.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/GMVAE.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/aligned_trajectory.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/aligned_trajectory.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/aligned_trajectory.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/aligned_trajectory.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/analysis.ipynb](../tetraha_mutation/H221F_tetraha/H123/gromacs/analysis.ipynb) | Notebook |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/anim.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/anim.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/backend_GMVAE/backend_GMVAE.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/clustering.ipynb](../tetraha_mutation/H221F_tetraha/H123/gromacs/clustering.ipynb) | Notebook |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/clustering.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/clustering.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/clustering_new.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/clustering_new.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/combined.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/combined.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/energy.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/energy.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/energy_combined.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/energy_combined.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/fluct_time.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/fluct_time.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/fluctuations.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/fluctuations.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/h_bonds.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/h_bonds.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/h_bonds.tcl](../tetraha_mutation/H221F_tetraha/H123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/important_hydrogen.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/important_hydrogen.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.23035794.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.23035794.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.26014103.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.26014103.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.26014161.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/mdout.26014161.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/nonpolar_contacts.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/nonpolar_contacts.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/production.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/production.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/protein_contact.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/protein_contact.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/protein_ligand_contact.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/protein_ligand_contact.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/reduced.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/reduced.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/rmsd.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/rmsd.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/rmsf.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/rmsf.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/salt_bridge.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/salt_bridge.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/salt_bridges.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/salt_bridges.py) | Python |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/step4.0_minimization.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/step4.1_equilibration.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/step5_production.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/step5_protein_ligand.mdp](../tetraha_mutation/H221F_tetraha/H123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/H123/gromacs/test.py](../tetraha_mutation/H221F_tetraha/H123/gromacs/test.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/addCrystPdb.py](../tetraha_mutation/H221F_tetraha/NOH123/addCrystPdb.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/checkfft.py](../tetraha_mutation/H221F_tetraha/NOH123/checkfft.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/glycan.yml](../tetraha_mutation/H221F_tetraha/NOH123/glycan.yml) | YAML configuration/environment |
| [tetraha_mutation/H221F_tetraha/NOH123/glycan_mod.yml](../tetraha_mutation/H221F_tetraha/NOH123/glycan_mod.yml) | YAML configuration/environment |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/GMVAE.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/GMVAE.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/aligned_trajectory.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/aligned_trajectory.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/aligned_trajectory.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/aligned_trajectory.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/analysis.ipynb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/analysis.ipynb) | Notebook |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/anim.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/anim.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering.ipynb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering.ipynb) | Notebook |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering_new.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/clustering_new.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/combined.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/combined.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/energy.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/energy.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/energy_combined.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/energy_combined.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/fluct_time.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/fluct_time.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/fluctuations.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/fluctuations.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/h_bonds.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/h_bonds.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/h_bonds.tcl](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/important_hydrogen.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/important_hydrogen.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/mdout.23035843.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/mdout.23035843.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/mdout.26014216.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/mdout.26014216.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/nonpolar_contacts.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/nonpolar_contacts.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/production.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/production.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/protein_contact.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/protein_contact.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/protein_ligand_contact.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/protein_ligand_contact.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/reduced.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/reduced.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/rmsd.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/rmsd.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/rmsf.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/rmsf.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/salt_bridge.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/salt_bridge.sb) | Slurm script |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/salt_bridges.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/salt_bridges.py) | Python |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/step4.0_minimization.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/step4.1_equilibration.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/step5_production.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/step5_protein_ligand.mdp](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [tetraha_mutation/H221F_tetraha/NOH123/gromacs/test.py](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/test.py) | Python |
| [tetraha_mutation/RMSF.py](../tetraha_mutation/RMSF.py) | Python |
| [tetraha_mutation/RMSF.sh](../tetraha_mutation/RMSF.sh) | Shell script |
| [tetraha_mutation/aligned_trajectory.py](../tetraha_mutation/aligned_trajectory.py) | Python |
| [tetraha_mutation/analysis.ipynb](../tetraha_mutation/analysis.ipynb) | Notebook |
| [tetraha_mutation/backend_GMVAE/backend_GMVAE.py](../tetraha_mutation/backend_GMVAE/backend_GMVAE.py) | Python |
| [tetraha_mutation/cluster_occurence.py](../tetraha_mutation/cluster_occurence.py) | Python |
| [tetraha_mutation/clustering.ipynb](../tetraha_mutation/clustering.ipynb) | Notebook |
| [tetraha_mutation/clustering.py](../tetraha_mutation/clustering.py) | Python |
| [tetraha_mutation/clustering_GMVAE.py](../tetraha_mutation/clustering_GMVAE.py) | Python |
| [tetraha_mutation/clustering_GMVAE.sh](../tetraha_mutation/clustering_GMVAE.sh) | Shell script |
| [tetraha_mutation/clustering_kmeans.py](../tetraha_mutation/clustering_kmeans.py) | Python |
| [tetraha_mutation/copy.sb](../tetraha_mutation/copy.sb) | Slurm script |
| [tetraha_mutation/energy.py](../tetraha_mutation/energy.py) | Python |
| [tetraha_mutation/energy_combined.sb](../tetraha_mutation/energy_combined.sb) | Slurm script |
| [tetraha_mutation/fluctuations.py](../tetraha_mutation/fluctuations.py) | Python |
| [tetraha_mutation/h_bond.py](../tetraha_mutation/h_bond.py) | Python |
| [tetraha_mutation/ligand_molecules_contact.py](../tetraha_mutation/ligand_molecules_contact.py) | Python |
| [tetraha_mutation/protein_ligand_contact.py](../tetraha_mutation/protein_ligand_contact.py) | Python |
| [tetraha_mutation/rmsd.py](../tetraha_mutation/rmsd.py) | Python |
| [tetraha_mutation/rmsd_docked.py](../tetraha_mutation/rmsd_docked.py) | Python |
| [tetraha_mutation/salt_bridge.py](../tetraha_mutation/salt_bridge.py) | Python |
| [tetraha_mutation/salt_bridge.sb](../tetraha_mutation/salt_bridge.sb) | Slurm script |
| [tetraha_mutation/salt_bridges.py](../tetraha_mutation/salt_bridges.py) | Python |
| [tetraha_mutation/scoring_function.py](../tetraha_mutation/scoring_function.py) | Python |
| [tetraha_mutation/scoring_function_discrete.py](../tetraha_mutation/scoring_function_discrete.py) | Python |
| [tetraha_mutation/snapshot_indices.py](../tetraha_mutation/snapshot_indices.py) | Python |
| [tetraha_mutation/step5_protein_ligand.mdp](../tetraha_mutation/step5_protein_ligand.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/addCrystPdb.py](../tetraha_mutation/tetraha/H123/addCrystPdb.py) | Python |
| [tetraha_mutation/tetraha/H123/checkfft.py](../tetraha_mutation/tetraha/H123/checkfft.py) | Python |
| [tetraha_mutation/tetraha/H123/glycan.yml](../tetraha_mutation/tetraha/H123/glycan.yml) | YAML configuration/environment |
| [tetraha_mutation/tetraha/H123/glycan_mod.yml](../tetraha_mutation/tetraha/H123/glycan_mod.yml) | YAML configuration/environment |
| [tetraha_mutation/tetraha/H123/gromacs/GMVAE.py](../tetraha_mutation/tetraha/H123/gromacs/GMVAE.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/aligned_trajectory.py](../tetraha_mutation/tetraha/H123/gromacs/aligned_trajectory.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/aligned_trajectory.sb](../tetraha_mutation/tetraha/H123/gromacs/aligned_trajectory.sb) | Slurm script |
| [tetraha_mutation/tetraha/H123/gromacs/analysis.ipynb](../tetraha_mutation/tetraha/H123/gromacs/analysis.ipynb) | Notebook |
| [tetraha_mutation/tetraha/H123/gromacs/anim.py](../tetraha_mutation/tetraha/H123/gromacs/anim.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/backend_GMVAE/backend_GMVAE.py](../tetraha_mutation/tetraha/H123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/clustering.ipynb](../tetraha_mutation/tetraha/H123/gromacs/clustering.ipynb) | Notebook |
| [tetraha_mutation/tetraha/H123/gromacs/clustering.py](../tetraha_mutation/tetraha/H123/gromacs/clustering.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/clustering_new.py](../tetraha_mutation/tetraha/H123/gromacs/clustering_new.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/energy_combined.sb](../tetraha_mutation/tetraha/H123/gromacs/energy_combined.sb) | Slurm script |
| [tetraha_mutation/tetraha/H123/gromacs/fluct_time.py](../tetraha_mutation/tetraha/H123/gromacs/fluct_time.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/h_bonds.sb](../tetraha_mutation/tetraha/H123/gromacs/h_bonds.sb) | Slurm script |
| [tetraha_mutation/tetraha/H123/gromacs/h_bonds.tcl](../tetraha_mutation/tetraha/H123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [tetraha_mutation/tetraha/H123/gromacs/important_hydrogen.py](../tetraha_mutation/tetraha/H123/gromacs/important_hydrogen.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/mdout.23035504.mdp](../tetraha_mutation/tetraha/H123/gromacs/mdout.23035504.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/mdout.28454580.mdp](../tetraha_mutation/tetraha/H123/gromacs/mdout.28454580.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/production.sb](../tetraha_mutation/tetraha/H123/gromacs/production.sb) | Slurm script |
| [tetraha_mutation/tetraha/H123/gromacs/protein_contact.py](../tetraha_mutation/tetraha/H123/gromacs/protein_contact.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/reduced.sb](../tetraha_mutation/tetraha/H123/gromacs/reduced.sb) | Slurm script |
| [tetraha_mutation/tetraha/H123/gromacs/rmsd.py](../tetraha_mutation/tetraha/H123/gromacs/rmsd.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/rmsf.py](../tetraha_mutation/tetraha/H123/gromacs/rmsf.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/salt_bridges.py](../tetraha_mutation/tetraha/H123/gromacs/salt_bridges.py) | Python |
| [tetraha_mutation/tetraha/H123/gromacs/step4.0_minimization.mdp](../tetraha_mutation/tetraha/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/step4.1_equilibration.mdp](../tetraha_mutation/tetraha/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/step5_production.mdp](../tetraha_mutation/tetraha/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/step5_protein_ligand.mdp](../tetraha_mutation/tetraha/H123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/H123/gromacs/test.py](../tetraha_mutation/tetraha/H123/gromacs/test.py) | Python |
| [tetraha_mutation/tetraha/NOH123/gromacs/aligned_trajectory.py](../tetraha_mutation/tetraha/NOH123/gromacs/aligned_trajectory.py) | Python |
| [tetraha_mutation/tetraha/NOH123/gromacs/aligned_trajectory.sb](../tetraha_mutation/tetraha/NOH123/gromacs/aligned_trajectory.sb) | Slurm script |
| [tetraha_mutation/tetraha/NOH123/gromacs/energy_combined.sb](../tetraha_mutation/tetraha/NOH123/gromacs/energy_combined.sb) | Slurm script |
| [tetraha_mutation/tetraha/NOH123/gromacs/h_bonds.sb](../tetraha_mutation/tetraha/NOH123/gromacs/h_bonds.sb) | Slurm script |
| [tetraha_mutation/tetraha/NOH123/gromacs/h_bonds.tcl](../tetraha_mutation/tetraha/NOH123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [tetraha_mutation/tetraha/NOH123/gromacs/important_hydrogen.py](../tetraha_mutation/tetraha/NOH123/gromacs/important_hydrogen.py) | Python |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454627.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454627.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454665.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454665.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454682.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454682.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454696.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454696.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454704.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454704.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454710.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/mdout.28454710.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/reduced.sb](../tetraha_mutation/tetraha/NOH123/gromacs/reduced.sb) | Slurm script |
| [tetraha_mutation/tetraha/NOH123/gromacs/salt_bridges.py](../tetraha_mutation/tetraha/NOH123/gromacs/salt_bridges.py) | Python |
| [tetraha_mutation/tetraha/NOH123/gromacs/step5_production.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [tetraha_mutation/tetraha/NOH123/gromacs/step5_protein_ligand.mdp](../tetraha_mutation/tetraha/NOH123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |

## hexamana_mutation (252 files)

| File | Type |
|---|---|
| [hexamana_mutation/H221F_hexamana/H109/addCrystPdb.py](../hexamana_mutation/H221F_hexamana/H109/addCrystPdb.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/checkfft.py](../hexamana_mutation/H221F_hexamana/H109/checkfft.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/glycan.yml](../hexamana_mutation/H221F_hexamana/H109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/H221F_hexamana/H109/glycan_mod.yml](../hexamana_mutation/H221F_hexamana/H109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/GMVAE.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/aligned_trajectory.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/aligned_trajectory.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/analysis.ipynb](../hexamana_mutation/H221F_hexamana/H109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/anim.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/anim.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/clustering.ipynb](../hexamana_mutation/H221F_hexamana/H109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/clustering.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/clustering.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/clustering_kmeans.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/clustering_new.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/combined.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/energy.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/energy.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/energy_combined.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/fluct_time.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/fluctuations.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/h_bonds.tcl](../hexamana_mutation/H221F_hexamana/H109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/important_hydrogen.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.23031717.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.23031717.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.23031728.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.23031728.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.26171486.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/mdout.26171486.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/nonpolar_contacts.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/production.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/protein_contact.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/protein_ligand_contact.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/rmsd.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/rmsd.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/rmsf.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/salt_bridge.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/salt_bridges.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/step5_production.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/H221F_hexamana/H109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/H109/gromacs/test.py](../hexamana_mutation/H221F_hexamana/H109/gromacs/test.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/addCrystPdb.py](../hexamana_mutation/H221F_hexamana/NOH109/addCrystPdb.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/checkfft.py](../hexamana_mutation/H221F_hexamana/NOH109/checkfft.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/glycan.yml](../hexamana_mutation/H221F_hexamana/NOH109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/H221F_hexamana/NOH109/glycan_mod.yml](../hexamana_mutation/H221F_hexamana/NOH109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/GMVAE.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/aligned_trajectory.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/aligned_trajectory.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/analysis.ipynb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/anim.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/anim.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering.ipynb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering_kmeans.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering_new.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/combined.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/energy.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/energy.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/energy_combined.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/fluct_time.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/fluctuations.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/h_bonds.tcl](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/important_hydrogen.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/mdout.23032776.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/mdout.23032776.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/mdout.26171839.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/mdout.26171839.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/nonpolar_contacts.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/production.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/protein_contact.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/protein_ligand_contact.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/rmsd.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/rmsd.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/rmsf.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/salt_bridge.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/salt_bridges.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/step5_production.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/H221F_hexamana/NOH109/gromacs/test.py](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/test.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/addCrystPdb.py](../hexamana_mutation/R312L_hexamana/H109/addCrystPdb.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/checkfft.py](../hexamana_mutation/R312L_hexamana/H109/checkfft.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/glycan.yml](../hexamana_mutation/R312L_hexamana/H109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/R312L_hexamana/H109/glycan_mod.yml](../hexamana_mutation/R312L_hexamana/H109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/GMVAE.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/aligned_trajectory.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/aligned_trajectory.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/analysis.ipynb](../hexamana_mutation/R312L_hexamana/H109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/anim.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/anim.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/clustering.ipynb](../hexamana_mutation/R312L_hexamana/H109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/clustering.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/clustering.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/clustering_kmeans.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/clustering_new.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/combined.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/energy.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/energy.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/energy_combined.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/fluct_time.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/fluctuations.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/h_bonds.tcl](../hexamana_mutation/R312L_hexamana/H109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/important_hydrogen.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.23032847.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.23032847.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.23033355.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.23033355.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.26171864.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/mdout.26171864.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/nonpolar_contacts.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/production.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/protein_contact.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/protein_ligand_contact.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/rmsd.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/rmsd.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/rmsf.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/salt_bridge.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/salt_bridges.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/step5_production.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/R312L_hexamana/H109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/H109/gromacs/test.py](../hexamana_mutation/R312L_hexamana/H109/gromacs/test.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/addCrystPdb.py](../hexamana_mutation/R312L_hexamana/NOH109/addCrystPdb.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/checkfft.py](../hexamana_mutation/R312L_hexamana/NOH109/checkfft.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/glycan.yml](../hexamana_mutation/R312L_hexamana/NOH109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/R312L_hexamana/NOH109/glycan_mod.yml](../hexamana_mutation/R312L_hexamana/NOH109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/GMVAE.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/aligned_trajectory.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/aligned_trajectory.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/analysis.ipynb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/anim.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/anim.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering.ipynb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering_kmeans.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering_new.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/combined.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/energy.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/energy.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/energy_combined.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/fluct_time.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/fluctuations.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/h_bonds.tcl](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/important_hydrogen.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/mdout.23033374.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/mdout.23033374.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/mdout.26172148.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/mdout.26172148.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/nonpolar_contacts.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/production.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/protein_contact.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/protein_ligand_contact.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/rmsd.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/rmsd.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/rmsf.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/salt_bridge.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/salt_bridges.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/step5_production.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/R312L_hexamana/NOH109/gromacs/test.py](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/test.py) | Python |
| [hexamana_mutation/RMSF.py](../hexamana_mutation/RMSF.py) | Python |
| [hexamana_mutation/aligned_trajectory.py](../hexamana_mutation/aligned_trajectory.py) | Python |
| [hexamana_mutation/analysis.ipynb](../hexamana_mutation/analysis.ipynb) | Notebook |
| [hexamana_mutation/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/cluster_occurence.py](../hexamana_mutation/cluster_occurence.py) | Python |
| [hexamana_mutation/clustering.ipynb](../hexamana_mutation/clustering.ipynb) | Notebook |
| [hexamana_mutation/clustering.py](../hexamana_mutation/clustering.py) | Python |
| [hexamana_mutation/clustering_GMVAE.py](../hexamana_mutation/clustering_GMVAE.py) | Python |
| [hexamana_mutation/clustering_GMVAE.sh](../hexamana_mutation/clustering_GMVAE.sh) | Shell script |
| [hexamana_mutation/clustering_gpu.py](../hexamana_mutation/clustering_gpu.py) | Python |
| [hexamana_mutation/clustering_kmeans.py](../hexamana_mutation/clustering_kmeans.py) | Python |
| [hexamana_mutation/energy.py](../hexamana_mutation/energy.py) | Python |
| [hexamana_mutation/fluctuations.py](../hexamana_mutation/fluctuations.py) | Python |
| [hexamana_mutation/h_bond.py](../hexamana_mutation/h_bond.py) | Python |
| [hexamana_mutation/hexamana/H109/addCrystPdb.py](../hexamana_mutation/hexamana/H109/addCrystPdb.py) | Python |
| [hexamana_mutation/hexamana/H109/analysis.ipynb](../hexamana_mutation/hexamana/H109/analysis.ipynb) | Notebook |
| [hexamana_mutation/hexamana/H109/checkfft.py](../hexamana_mutation/hexamana/H109/checkfft.py) | Python |
| [hexamana_mutation/hexamana/H109/clustering.ipynb](../hexamana_mutation/hexamana/H109/clustering.ipynb) | Notebook |
| [hexamana_mutation/hexamana/H109/glycan.yml](../hexamana_mutation/hexamana/H109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/hexamana/H109/glycan_mod.yml](../hexamana_mutation/hexamana/H109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/hexamana/H109/gromacs/GMVAE.py](../hexamana_mutation/hexamana/H109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/Untitled.ipynb](../hexamana_mutation/hexamana/H109/gromacs/Untitled.ipynb) | Notebook |
| [hexamana_mutation/hexamana/H109/gromacs/aligned_trajectory.py](../hexamana_mutation/hexamana/H109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/aligned_trajectory.sb](../hexamana_mutation/hexamana/H109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/analysis.ipynb](../hexamana_mutation/hexamana/H109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/hexamana/H109/gromacs/anim.py](../hexamana_mutation/hexamana/H109/gromacs/anim.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/hexamana/H109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/clustering.ipynb](../hexamana_mutation/hexamana/H109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/hexamana/H109/gromacs/clustering.py](../hexamana_mutation/hexamana/H109/gromacs/clustering.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/clustering_kmeans.py](../hexamana_mutation/hexamana/H109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/clustering_new.py](../hexamana_mutation/hexamana/H109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/combined.sb](../hexamana_mutation/hexamana/H109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/energy.py](../hexamana_mutation/hexamana/H109/gromacs/energy.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/energy_combined.sb](../hexamana_mutation/hexamana/H109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/fluct_time.py](../hexamana_mutation/hexamana/H109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/fluctuations.py](../hexamana_mutation/hexamana/H109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/h_bonds.tcl](../hexamana_mutation/hexamana/H109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/hexamana/H109/gromacs/important_hydrogen.py](../hexamana_mutation/hexamana/H109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/mdout.23035381.mdp](../hexamana_mutation/hexamana/H109/gromacs/mdout.23035381.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/mdout.26170840.mdp](../hexamana_mutation/hexamana/H109/gromacs/mdout.26170840.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/nonpolar_contacts.py](../hexamana_mutation/hexamana/H109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/production.sb](../hexamana_mutation/hexamana/H109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/protein_contact.py](../hexamana_mutation/hexamana/H109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/protein_ligand_contact.py](../hexamana_mutation/hexamana/H109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/hexamana/H109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/rmsf.py](../hexamana_mutation/hexamana/H109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/salt_bridge.sb](../hexamana_mutation/hexamana/H109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/hexamana/H109/gromacs/salt_bridges.py](../hexamana_mutation/hexamana/H109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/hexamana/H109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/hexamana/H109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/hexamana/H109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/step5_production.mdp](../hexamana_mutation/hexamana/H109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/hexamana/H109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/H109/gromacs/test.py](../hexamana_mutation/hexamana/H109/gromacs/test.py) | Python |
| [hexamana_mutation/hexamana/NOH109/addCrystPdb.py](../hexamana_mutation/hexamana/NOH109/addCrystPdb.py) | Python |
| [hexamana_mutation/hexamana/NOH109/checkfft.py](../hexamana_mutation/hexamana/NOH109/checkfft.py) | Python |
| [hexamana_mutation/hexamana/NOH109/glycan.yml](../hexamana_mutation/hexamana/NOH109/glycan.yml) | YAML configuration/environment |
| [hexamana_mutation/hexamana/NOH109/glycan_mod.yml](../hexamana_mutation/hexamana/NOH109/glycan_mod.yml) | YAML configuration/environment |
| [hexamana_mutation/hexamana/NOH109/gromacs/GMVAE.py](../hexamana_mutation/hexamana/NOH109/gromacs/GMVAE.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/aligned_trajectory.py](../hexamana_mutation/hexamana/NOH109/gromacs/aligned_trajectory.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/aligned_trajectory.sb](../hexamana_mutation/hexamana/NOH109/gromacs/aligned_trajectory.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/analysis.ipynb](../hexamana_mutation/hexamana/NOH109/gromacs/analysis.ipynb) | Notebook |
| [hexamana_mutation/hexamana/NOH109/gromacs/anim.py](../hexamana_mutation/hexamana/NOH109/gromacs/anim.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py](../hexamana_mutation/hexamana/NOH109/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/clustering.ipynb](../hexamana_mutation/hexamana/NOH109/gromacs/clustering.ipynb) | Notebook |
| [hexamana_mutation/hexamana/NOH109/gromacs/clustering.py](../hexamana_mutation/hexamana/NOH109/gromacs/clustering.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/clustering_kmeans.py](../hexamana_mutation/hexamana/NOH109/gromacs/clustering_kmeans.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/clustering_new.py](../hexamana_mutation/hexamana/NOH109/gromacs/clustering_new.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/combined.sb](../hexamana_mutation/hexamana/NOH109/gromacs/combined.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/energy.py](../hexamana_mutation/hexamana/NOH109/gromacs/energy.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/energy_combined.sb](../hexamana_mutation/hexamana/NOH109/gromacs/energy_combined.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/fluct_time.py](../hexamana_mutation/hexamana/NOH109/gromacs/fluct_time.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/fluctuations.py](../hexamana_mutation/hexamana/NOH109/gromacs/fluctuations.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/h_bonds.tcl](../hexamana_mutation/hexamana/NOH109/gromacs/h_bonds.tcl) | Tcl/VMD |
| [hexamana_mutation/hexamana/NOH109/gromacs/important_hydrogen.py](../hexamana_mutation/hexamana/NOH109/gromacs/important_hydrogen.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/mdout.23033717.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/mdout.23033717.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/mdout.26171469.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/mdout.26171469.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/nonpolar_contacts.py](../hexamana_mutation/hexamana/NOH109/gromacs/nonpolar_contacts.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/production.sb](../hexamana_mutation/hexamana/NOH109/gromacs/production.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/protein_contact.py](../hexamana_mutation/hexamana/NOH109/gromacs/protein_contact.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/protein_ligand_contact.py](../hexamana_mutation/hexamana/NOH109/gromacs/protein_ligand_contact.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/hexamana/NOH109/gromacs/reduced.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/rmsd.py](../hexamana_mutation/hexamana/NOH109/gromacs/rmsd.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/rmsf.py](../hexamana_mutation/hexamana/NOH109/gromacs/rmsf.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/salt_bridge.sb](../hexamana_mutation/hexamana/NOH109/gromacs/salt_bridge.sb) | Slurm script |
| [hexamana_mutation/hexamana/NOH109/gromacs/salt_bridges.py](../hexamana_mutation/hexamana/NOH109/gromacs/salt_bridges.py) | Python |
| [hexamana_mutation/hexamana/NOH109/gromacs/step4.0_minimization.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/step4.1_equilibration.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/step5_production.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/step5_production.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/step5_protein_ligand.mdp](../hexamana_mutation/hexamana/NOH109/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [hexamana_mutation/hexamana/NOH109/gromacs/test.py](../hexamana_mutation/hexamana/NOH109/gromacs/test.py) | Python |
| [hexamana_mutation/hexamana/clustering_kmeans.py](../hexamana_mutation/hexamana/clustering_kmeans.py) | Python |
| [hexamana_mutation/ligand_molecules_contact.py](../hexamana_mutation/ligand_molecules_contact.py) | Python |
| [hexamana_mutation/protein_ligand_contact.py](../hexamana_mutation/protein_ligand_contact.py) | Python |
| [hexamana_mutation/pytorch.sh](../hexamana_mutation/pytorch.sh) | Shell script |
| [hexamana_mutation/rmsd.py](../hexamana_mutation/rmsd.py) | Python |
| [hexamana_mutation/rmsd_docked.py](../hexamana_mutation/rmsd_docked.py) | Python |
| [hexamana_mutation/run-pytorch-gpu-shared.sh](../hexamana_mutation/run-pytorch-gpu-shared.sh) | Shell script |
| [hexamana_mutation/salt_bridge.py](../hexamana_mutation/salt_bridge.py) | Python |
| [hexamana_mutation/salt_bridges.py](../hexamana_mutation/salt_bridges.py) | Python |
| [hexamana_mutation/scoring_function.py](../hexamana_mutation/scoring_function.py) | Python |
| [hexamana_mutation/scoring_function_discrete.py](../hexamana_mutation/scoring_function_discrete.py) | Python |
| [hexamana_mutation/snapshot_indices.py](../hexamana_mutation/snapshot_indices.py) | Python |

## fourha_mutation (159 files)

| File | Type |
|---|---|
| [fourha_mutation/H221F_fourha/H123/addCrystPdb.py](../fourha_mutation/H221F_fourha/H123/addCrystPdb.py) | Python |
| [fourha_mutation/H221F_fourha/H123/checkfft.py](../fourha_mutation/H221F_fourha/H123/checkfft.py) | Python |
| [fourha_mutation/H221F_fourha/H123/glycan.yml](../fourha_mutation/H221F_fourha/H123/glycan.yml) | YAML configuration/environment |
| [fourha_mutation/H221F_fourha/H123/glycan_mod.yml](../fourha_mutation/H221F_fourha/H123/glycan_mod.yml) | YAML configuration/environment |
| [fourha_mutation/H221F_fourha/H123/gromacs/aligned_trajectory.py](../fourha_mutation/H221F_fourha/H123/gromacs/aligned_trajectory.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/aligned_trajectory.sb](../fourha_mutation/H221F_fourha/H123/gromacs/aligned_trajectory.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/analysis.ipynb](../fourha_mutation/H221F_fourha/H123/gromacs/analysis.ipynb) | Notebook |
| [fourha_mutation/H221F_fourha/H123/gromacs/backend_GMVAE/backend_GMVAE.py](../fourha_mutation/H221F_fourha/H123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/clustering.ipynb](../fourha_mutation/H221F_fourha/H123/gromacs/clustering.ipynb) | Notebook |
| [fourha_mutation/H221F_fourha/H123/gromacs/combined.sb](../fourha_mutation/H221F_fourha/H123/gromacs/combined.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/energy.py](../fourha_mutation/H221F_fourha/H123/gromacs/energy.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/energy_combined.sb](../fourha_mutation/H221F_fourha/H123/gromacs/energy_combined.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/fluctuations.py](../fourha_mutation/H221F_fourha/H123/gromacs/fluctuations.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/h_bonds.tcl](../fourha_mutation/H221F_fourha/H123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [fourha_mutation/H221F_fourha/H123/gromacs/important_hydrogen.py](../fourha_mutation/H221F_fourha/H123/gromacs/important_hydrogen.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/mdout.24072206.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/mdout.24072206.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/H123/gromacs/mdout.25549230.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/mdout.25549230.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/H123/gromacs/nonpolar_contacts.py](../fourha_mutation/H221F_fourha/H123/gromacs/nonpolar_contacts.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/production.sb](../fourha_mutation/H221F_fourha/H123/gromacs/production.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/protein_ligand_contact.py](../fourha_mutation/H221F_fourha/H123/gromacs/protein_ligand_contact.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/reduced.sb](../fourha_mutation/H221F_fourha/H123/gromacs/reduced.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/rmsd.py](../fourha_mutation/H221F_fourha/H123/gromacs/rmsd.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/rmsf.py](../fourha_mutation/H221F_fourha/H123/gromacs/rmsf.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/salt_bridge.sb](../fourha_mutation/H221F_fourha/H123/gromacs/salt_bridge.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/H123/gromacs/salt_bridge.tcl](../fourha_mutation/H221F_fourha/H123/gromacs/salt_bridge.tcl) | Tcl/VMD |
| [fourha_mutation/H221F_fourha/H123/gromacs/salt_bridges.py](../fourha_mutation/H221F_fourha/H123/gromacs/salt_bridges.py) | Python |
| [fourha_mutation/H221F_fourha/H123/gromacs/step4.0_minimization.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/H123/gromacs/step4.1_equilibration.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/H123/gromacs/step5_production.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/H123/gromacs/step5_protein_ligand.mdp](../fourha_mutation/H221F_fourha/H123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/addCrystPdb.py](../fourha_mutation/H221F_fourha/NOH123/addCrystPdb.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/checkfft.py](../fourha_mutation/H221F_fourha/NOH123/checkfft.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/glycan.yml](../fourha_mutation/H221F_fourha/NOH123/glycan.yml) | YAML configuration/environment |
| [fourha_mutation/H221F_fourha/NOH123/glycan_mod.yml](../fourha_mutation/H221F_fourha/NOH123/glycan_mod.yml) | YAML configuration/environment |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/aligned_trajectory.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/aligned_trajectory.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/aligned_trajectory.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/aligned_trajectory.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/analysis.ipynb](../fourha_mutation/H221F_fourha/NOH123/gromacs/analysis.ipynb) | Notebook |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/clustering.ipynb](../fourha_mutation/H221F_fourha/NOH123/gromacs/clustering.ipynb) | Notebook |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/combined.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/combined.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/energy.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/energy.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/energy_combined.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/energy_combined.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/fluctuations.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/fluctuations.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/h_bonds.tcl](../fourha_mutation/H221F_fourha/NOH123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/important_hydrogen.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/important_hydrogen.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/mdout.24072216.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/mdout.24072216.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/mdout.25549236.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/mdout.25549236.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/nonpolar_contacts.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/nonpolar_contacts.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/production.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/production.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/protein_ligand_contact.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/protein_ligand_contact.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/reduced.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/reduced.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/rmsd.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/rmsd.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/rmsf.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/rmsf.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridge.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridge.sb) | Slurm script |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridge.tcl](../fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridge.tcl) | Tcl/VMD |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridges.py](../fourha_mutation/H221F_fourha/NOH123/gromacs/salt_bridges.py) | Python |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/step4.0_minimization.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/step4.1_equilibration.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/step5_production.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [fourha_mutation/H221F_fourha/NOH123/gromacs/step5_protein_ligand.mdp](../fourha_mutation/H221F_fourha/NOH123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [fourha_mutation/RMSF.py](../fourha_mutation/RMSF.py) | Python |
| [fourha_mutation/aligned_trajectory.py](../fourha_mutation/aligned_trajectory.py) | Python |
| [fourha_mutation/backend_GMVAE/backend_GMVAE.py](../fourha_mutation/backend_GMVAE/backend_GMVAE.py) | Python |
| [fourha_mutation/cluster_occurence.py](../fourha_mutation/cluster_occurence.py) | Python |
| [fourha_mutation/clustering.py](../fourha_mutation/clustering.py) | Python |
| [fourha_mutation/clustering_rmsd.sb](../fourha_mutation/clustering_rmsd.sb) | Slurm script |
| [fourha_mutation/copy.sb](../fourha_mutation/copy.sb) | Slurm script |
| [fourha_mutation/energy.py](../fourha_mutation/energy.py) | Python |
| [fourha_mutation/energy_combined.sb](../fourha_mutation/energy_combined.sb) | Slurm script |
| [fourha_mutation/fluctuations.py](../fourha_mutation/fluctuations.py) | Python |
| [fourha_mutation/fourha/H123/addCrystPdb.py](../fourha_mutation/fourha/H123/addCrystPdb.py) | Python |
| [fourha_mutation/fourha/H123/checkfft.py](../fourha_mutation/fourha/H123/checkfft.py) | Python |
| [fourha_mutation/fourha/H123/glycan.yml](../fourha_mutation/fourha/H123/glycan.yml) | YAML configuration/environment |
| [fourha_mutation/fourha/H123/glycan_mod.yml](../fourha_mutation/fourha/H123/glycan_mod.yml) | YAML configuration/environment |
| [fourha_mutation/fourha/H123/gromacs/aligned_trajectory.py](../fourha_mutation/fourha/H123/gromacs/aligned_trajectory.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/aligned_trajectory.sb](../fourha_mutation/fourha/H123/gromacs/aligned_trajectory.sb) | Slurm script |
| [fourha_mutation/fourha/H123/gromacs/analysis.ipynb](../fourha_mutation/fourha/H123/gromacs/analysis.ipynb) | Notebook |
| [fourha_mutation/fourha/H123/gromacs/backend_GMVAE/backend_GMVAE.py](../fourha_mutation/fourha/H123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/clustering.ipynb](../fourha_mutation/fourha/H123/gromacs/clustering.ipynb) | Notebook |
| [fourha_mutation/fourha/H123/gromacs/combined.sb](../fourha_mutation/fourha/H123/gromacs/combined.sb) | Slurm script |
| [fourha_mutation/fourha/H123/gromacs/energy.py](../fourha_mutation/fourha/H123/gromacs/energy.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/energy_combined.sb](../fourha_mutation/fourha/H123/gromacs/energy_combined.sb) | Slurm script |
| [fourha_mutation/fourha/H123/gromacs/fluctuations.py](../fourha_mutation/fourha/H123/gromacs/fluctuations.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/h_bonds.tcl](../fourha_mutation/fourha/H123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [fourha_mutation/fourha/H123/gromacs/important_hydrogen.py](../fourha_mutation/fourha/H123/gromacs/important_hydrogen.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/mdout..mdp](../fourha_mutation/fourha/H123/gromacs/mdout..mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.24072105.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.24072105.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25377307.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25377307.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25377641.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25377641.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25377648.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25377648.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25455798.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25455798.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25549222.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25549222.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/mdout.25549225.mdp](../fourha_mutation/fourha/H123/gromacs/mdout.25549225.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/nonpolar_contacts.py](../fourha_mutation/fourha/H123/gromacs/nonpolar_contacts.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/production.sb](../fourha_mutation/fourha/H123/gromacs/production.sb) | Slurm script |
| [fourha_mutation/fourha/H123/gromacs/protein_ligand_contact.py](../fourha_mutation/fourha/H123/gromacs/protein_ligand_contact.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/python_files/energy.py](../fourha_mutation/fourha/H123/gromacs/python_files/energy.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/python_files/h_bonds.py](../fourha_mutation/fourha/H123/gromacs/python_files/h_bonds.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/python_files/hydrogen.py](../fourha_mutation/fourha/H123/gromacs/python_files/hydrogen.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/python_files/salt_bridge.py](../fourha_mutation/fourha/H123/gromacs/python_files/salt_bridge.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/python_files/salt_bridges.py](../fourha_mutation/fourha/H123/gromacs/python_files/salt_bridges.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/rmsd.py](../fourha_mutation/fourha/H123/gromacs/rmsd.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/rmsf.py](../fourha_mutation/fourha/H123/gromacs/rmsf.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/salt_bridge.sb](../fourha_mutation/fourha/H123/gromacs/salt_bridge.sb) | Slurm script |
| [fourha_mutation/fourha/H123/gromacs/salt_bridge.tcl](../fourha_mutation/fourha/H123/gromacs/salt_bridge.tcl) | Tcl/VMD |
| [fourha_mutation/fourha/H123/gromacs/salt_bridges.py](../fourha_mutation/fourha/H123/gromacs/salt_bridges.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/scoring_function.py](../fourha_mutation/fourha/H123/gromacs/scoring_function.py) | Python |
| [fourha_mutation/fourha/H123/gromacs/step4.0_minimization.mdp](../fourha_mutation/fourha/H123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/step4.1_equilibration.mdp](../fourha_mutation/fourha/H123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/step5_production.mdp](../fourha_mutation/fourha/H123/gromacs/step5_production.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/step5_protein_ligand.mdp](../fourha_mutation/fourha/H123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/H123/gromacs/test.tcl](../fourha_mutation/fourha/H123/gromacs/test.tcl) | Tcl/VMD |
| [fourha_mutation/fourha/NOH123/addCrystPdb.py](../fourha_mutation/fourha/NOH123/addCrystPdb.py) | Python |
| [fourha_mutation/fourha/NOH123/checkfft.py](../fourha_mutation/fourha/NOH123/checkfft.py) | Python |
| [fourha_mutation/fourha/NOH123/glycan.yml](../fourha_mutation/fourha/NOH123/glycan.yml) | YAML configuration/environment |
| [fourha_mutation/fourha/NOH123/glycan_mod.yml](../fourha_mutation/fourha/NOH123/glycan_mod.yml) | YAML configuration/environment |
| [fourha_mutation/fourha/NOH123/gromacs/aligned_trajectory.py](../fourha_mutation/fourha/NOH123/gromacs/aligned_trajectory.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/aligned_trajectory.sb](../fourha_mutation/fourha/NOH123/gromacs/aligned_trajectory.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/analysis.ipynb](../fourha_mutation/fourha/NOH123/gromacs/analysis.ipynb) | Notebook |
| [fourha_mutation/fourha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py](../fourha_mutation/fourha/NOH123/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/clustering.ipynb](../fourha_mutation/fourha/NOH123/gromacs/clustering.ipynb) | Notebook |
| [fourha_mutation/fourha/NOH123/gromacs/combined.sb](../fourha_mutation/fourha/NOH123/gromacs/combined.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/energy.py](../fourha_mutation/fourha/NOH123/gromacs/energy.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/energy_combined.sb](../fourha_mutation/fourha/NOH123/gromacs/energy_combined.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/fluctuations.py](../fourha_mutation/fourha/NOH123/gromacs/fluctuations.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/h_bonds.tcl](../fourha_mutation/fourha/NOH123/gromacs/h_bonds.tcl) | Tcl/VMD |
| [fourha_mutation/fourha/NOH123/gromacs/important_hydrogen.py](../fourha_mutation/fourha/NOH123/gromacs/important_hydrogen.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.24072114.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.24072114.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.24072185.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.24072185.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.25490831.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.25490831.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.25490863.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.25490863.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.25490879.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.25490879.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/mdout.25549227.mdp](../fourha_mutation/fourha/NOH123/gromacs/mdout.25549227.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/nonpolar_contacts.py](../fourha_mutation/fourha/NOH123/gromacs/nonpolar_contacts.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/production.sb](../fourha_mutation/fourha/NOH123/gromacs/production.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/protein_ligand_contact.py](../fourha_mutation/fourha/NOH123/gromacs/protein_ligand_contact.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/reduced.sb](../fourha_mutation/fourha/NOH123/gromacs/reduced.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/rmsd.py](../fourha_mutation/fourha/NOH123/gromacs/rmsd.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/rmsf.py](../fourha_mutation/fourha/NOH123/gromacs/rmsf.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/salt_bridge.sb](../fourha_mutation/fourha/NOH123/gromacs/salt_bridge.sb) | Slurm script |
| [fourha_mutation/fourha/NOH123/gromacs/salt_bridge.tcl](../fourha_mutation/fourha/NOH123/gromacs/salt_bridge.tcl) | Tcl/VMD |
| [fourha_mutation/fourha/NOH123/gromacs/salt_bridges.py](../fourha_mutation/fourha/NOH123/gromacs/salt_bridges.py) | Python |
| [fourha_mutation/fourha/NOH123/gromacs/step4.0_minimization.mdp](../fourha_mutation/fourha/NOH123/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/step4.1_equilibration.mdp](../fourha_mutation/fourha/NOH123/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/step5_production.mdp](../fourha_mutation/fourha/NOH123/gromacs/step5_production.mdp) | GROMACS parameters |
| [fourha_mutation/fourha/NOH123/gromacs/step5_protein_ligand.mdp](../fourha_mutation/fourha/NOH123/gromacs/step5_protein_ligand.mdp) | GROMACS parameters |
| [fourha_mutation/h_bond.py](../fourha_mutation/h_bond.py) | Python |
| [fourha_mutation/ligand_molecules_contact.py](../fourha_mutation/ligand_molecules_contact.py) | Python |
| [fourha_mutation/protein_ligand_contact.py](../fourha_mutation/protein_ligand_contact.py) | Python |
| [fourha_mutation/rmsd.py](../fourha_mutation/rmsd.py) | Python |
| [fourha_mutation/rmsd.sb](../fourha_mutation/rmsd.sb) | Slurm script |
| [fourha_mutation/rmsd_docked.py](../fourha_mutation/rmsd_docked.py) | Python |
| [fourha_mutation/salt_bridge.py](../fourha_mutation/salt_bridge.py) | Python |
| [fourha_mutation/salt_bridge.sb](../fourha_mutation/salt_bridge.sb) | Slurm script |
| [fourha_mutation/salt_bridges.py](../fourha_mutation/salt_bridges.py) | Python |
| [fourha_mutation/scores_overall_metrics.sh](../fourha_mutation/scores_overall_metrics.sh) | Shell script |
| [fourha_mutation/scoring.sh](../fourha_mutation/scoring.sh) | Shell script |
| [fourha_mutation/scoring_function.py](../fourha_mutation/scoring_function.py) | Python |
| [fourha_mutation/scoring_function_discrete.py](../fourha_mutation/scoring_function_discrete.py) | Python |

## N136D (96 files)

| File | Type |
|---|---|
| [N136D/N136D_MGMG/h_130/addCrystPdb.py](../N136D/N136D_MGMG/h_130/addCrystPdb.py) | Python |
| [N136D/N136D_MGMG/h_130/checkfft.py](../N136D/N136D_MGMG/h_130/checkfft.py) | Python |
| [N136D/N136D_MGMG/h_130/glycan.yml](../N136D/N136D_MGMG/h_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/h_130/glycan_mod.yml](../N136D/N136D_MGMG/h_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/h_130/gromacs/analysis.ipynb](../N136D/N136D_MGMG/h_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MGMG/h_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MGMG/h_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MGMG/h_130/gromacs/clustering.ipynb](../N136D/N136D_MGMG/h_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MGMG/h_130/gromacs/combined.sb](../N136D/N136D_MGMG/h_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MGMG/h_130/gromacs/mdout.24072411.mdp](../N136D/N136D_MGMG/h_130/gromacs/mdout.24072411.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/h_130/gromacs/production.sb](../N136D/N136D_MGMG/h_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MGMG/h_130/gromacs/reduced.sb](../N136D/N136D_MGMG/h_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MGMG/h_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MGMG/h_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/h_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MGMG/h_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/h_130/gromacs/step5_production.mdp](../N136D/N136D_MGMG/h_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/addCrystPdb.py](../N136D/N136D_MGMG/noh_130/addCrystPdb.py) | Python |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/addCrystPdb.py](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/addCrystPdb.py) | Python |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/checkfft.py](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/checkfft.py) | Python |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/glycan.yml](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/glycan_mod.yml](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step4.0_minimization.mdp](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step5_production.mdp](../N136D/N136D_MGMG/noh_130/charmm-gui-8952024542/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/checkfft.py](../N136D/N136D_MGMG/noh_130/checkfft.py) | Python |
| [N136D/N136D_MGMG/noh_130/glycan.yml](../N136D/N136D_MGMG/noh_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/noh_130/glycan_mod.yml](../N136D/N136D_MGMG/noh_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MGMG/noh_130/gromacs/analysis.ipynb](../N136D/N136D_MGMG/noh_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MGMG/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MGMG/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MGMG/noh_130/gromacs/clustering.ipynb](../N136D/N136D_MGMG/noh_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MGMG/noh_130/gromacs/combined.sb](../N136D/N136D_MGMG/noh_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MGMG/noh_130/gromacs/mdout.24072436.mdp](../N136D/N136D_MGMG/noh_130/gromacs/mdout.24072436.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/gromacs/production.sb](../N136D/N136D_MGMG/noh_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MGMG/noh_130/gromacs/reduced.sb](../N136D/N136D_MGMG/noh_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MGMG/noh_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MGMG/noh_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MGMG/noh_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MGMG/noh_130/gromacs/step5_production.mdp](../N136D/N136D_MGMG/noh_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/h_130/addCrystPdb.py](../N136D/N136D_MMGG/h_130/addCrystPdb.py) | Python |
| [N136D/N136D_MMGG/h_130/checkfft.py](../N136D/N136D_MMGG/h_130/checkfft.py) | Python |
| [N136D/N136D_MMGG/h_130/glycan.yml](../N136D/N136D_MMGG/h_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MMGG/h_130/glycan_mod.yml](../N136D/N136D_MMGG/h_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MMGG/h_130/gromacs/analysis.ipynb](../N136D/N136D_MMGG/h_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MMGG/h_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MMGG/h_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MMGG/h_130/gromacs/clustering.ipynb](../N136D/N136D_MMGG/h_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MMGG/h_130/gromacs/combined.sb](../N136D/N136D_MMGG/h_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MMGG/h_130/gromacs/mdout.24072349.mdp](../N136D/N136D_MMGG/h_130/gromacs/mdout.24072349.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/h_130/gromacs/production.sb](../N136D/N136D_MMGG/h_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MMGG/h_130/gromacs/reduced.sb](../N136D/N136D_MMGG/h_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MMGG/h_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MMGG/h_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/h_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MMGG/h_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/h_130/gromacs/step5_production.mdp](../N136D/N136D_MMGG/h_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/noh_130/addCrystPdb.py](../N136D/N136D_MMGG/noh_130/addCrystPdb.py) | Python |
| [N136D/N136D_MMGG/noh_130/checkfft.py](../N136D/N136D_MMGG/noh_130/checkfft.py) | Python |
| [N136D/N136D_MMGG/noh_130/glycan.yml](../N136D/N136D_MMGG/noh_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MMGG/noh_130/glycan_mod.yml](../N136D/N136D_MMGG/noh_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MMGG/noh_130/gromacs/analysis.ipynb](../N136D/N136D_MMGG/noh_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MMGG/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MMGG/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MMGG/noh_130/gromacs/clustering.ipynb](../N136D/N136D_MMGG/noh_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MMGG/noh_130/gromacs/combined.sb](../N136D/N136D_MMGG/noh_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MMGG/noh_130/gromacs/mdout.24072353.mdp](../N136D/N136D_MMGG/noh_130/gromacs/mdout.24072353.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/noh_130/gromacs/production.sb](../N136D/N136D_MMGG/noh_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MMGG/noh_130/gromacs/reduced.sb](../N136D/N136D_MMGG/noh_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MMGG/noh_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MMGG/noh_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/noh_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MMGG/noh_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MMGG/noh_130/gromacs/step5_production.mdp](../N136D/N136D_MMGG/noh_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/h_130/addCrystPdb.py](../N136D/N136D_MMMM/h_130/addCrystPdb.py) | Python |
| [N136D/N136D_MMMM/h_130/checkfft.py](../N136D/N136D_MMMM/h_130/checkfft.py) | Python |
| [N136D/N136D_MMMM/h_130/glycan.yml](../N136D/N136D_MMMM/h_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MMMM/h_130/glycan_mod.yml](../N136D/N136D_MMMM/h_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MMMM/h_130/gromacs/analysis.ipynb](../N136D/N136D_MMMM/h_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MMMM/h_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MMMM/h_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MMMM/h_130/gromacs/clustering.ipynb](../N136D/N136D_MMMM/h_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MMMM/h_130/gromacs/combined.sb](../N136D/N136D_MMMM/h_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MMMM/h_130/gromacs/mdout.24072273.mdp](../N136D/N136D_MMMM/h_130/gromacs/mdout.24072273.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/h_130/gromacs/production.sb](../N136D/N136D_MMMM/h_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MMMM/h_130/gromacs/reduced.sb](../N136D/N136D_MMMM/h_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MMMM/h_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MMMM/h_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/h_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MMMM/h_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/h_130/gromacs/step5_production.mdp](../N136D/N136D_MMMM/h_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/noh_130/addCrystPdb.py](../N136D/N136D_MMMM/noh_130/addCrystPdb.py) | Python |
| [N136D/N136D_MMMM/noh_130/checkfft.py](../N136D/N136D_MMMM/noh_130/checkfft.py) | Python |
| [N136D/N136D_MMMM/noh_130/glycan.yml](../N136D/N136D_MMMM/noh_130/glycan.yml) | YAML configuration/environment |
| [N136D/N136D_MMMM/noh_130/glycan_mod.yml](../N136D/N136D_MMMM/noh_130/glycan_mod.yml) | YAML configuration/environment |
| [N136D/N136D_MMMM/noh_130/gromacs/Untitled.ipynb](../N136D/N136D_MMMM/noh_130/gromacs/Untitled.ipynb) | Notebook |
| [N136D/N136D_MMMM/noh_130/gromacs/analysis.ipynb](../N136D/N136D_MMMM/noh_130/gromacs/analysis.ipynb) | Notebook |
| [N136D/N136D_MMMM/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py](../N136D/N136D_MMMM/noh_130/gromacs/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/N136D_MMMM/noh_130/gromacs/clustering.ipynb](../N136D/N136D_MMMM/noh_130/gromacs/clustering.ipynb) | Notebook |
| [N136D/N136D_MMMM/noh_130/gromacs/combined.sb](../N136D/N136D_MMMM/noh_130/gromacs/combined.sb) | Slurm script |
| [N136D/N136D_MMMM/noh_130/gromacs/mdout.24072292.mdp](../N136D/N136D_MMMM/noh_130/gromacs/mdout.24072292.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/noh_130/gromacs/production.sb](../N136D/N136D_MMMM/noh_130/gromacs/production.sb) | Slurm script |
| [N136D/N136D_MMMM/noh_130/gromacs/reduced.sb](../N136D/N136D_MMMM/noh_130/gromacs/reduced.sb) | Slurm script |
| [N136D/N136D_MMMM/noh_130/gromacs/step4.0_minimization.mdp](../N136D/N136D_MMMM/noh_130/gromacs/step4.0_minimization.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/noh_130/gromacs/step4.1_equilibration.mdp](../N136D/N136D_MMMM/noh_130/gromacs/step4.1_equilibration.mdp) | GROMACS parameters |
| [N136D/N136D_MMMM/noh_130/gromacs/step5_production.mdp](../N136D/N136D_MMMM/noh_130/gromacs/step5_production.mdp) | GROMACS parameters |
| [N136D/Untitled.ipynb](../N136D/Untitled.ipynb) | Notebook |
| [N136D/analysis.ipynb](../N136D/analysis.ipynb) | Notebook |
| [N136D/backend_GMVAE/backend_GMVAE.py](../N136D/backend_GMVAE/backend_GMVAE.py) | Python |
| [N136D/clustering.ipynb](../N136D/clustering.ipynb) | Notebook |
