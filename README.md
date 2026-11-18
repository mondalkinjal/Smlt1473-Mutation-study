# Effect of Mutations on Smlt1473 Binding to Various Substrates Using Molecular Dynamics Simulations

Code and simulation input files accompanying the manuscript:

> **Effect of Mutations on Smlt1473 Binding to Various Substrates Using Molecular Dynamics Simulations**
> *J. Phys. Chem. B* **2025**, 129 (16), 3948.
> Manuscript: [https://pubs.acs.org/jpcbfk/article/129/16/3948/3650020/Effect-of-Mutations-on-Smlt1473-Binding-to-Various](https://pubs.acs.org/jpcbfk/article/129/16/3948/3650020/Effect-of-Mutations-on-Smlt1473-Binding-to-Various)

## Repository layout

| Folder | Contents |
|---|---|
| `apo/` | Apo Smlt1473 (WT, H221F, R312L) simulations at pH 5 and pH 9; RMSD/RMSF/fluctuation analysis and pKa extraction |
| `tetraha_mutation/` | Tetrasaccharide hyaluronic acid (HA4) complexes, WT and H221F |
| `hexamana_mutation/` | Hexamannuronate (ManA6) complexes, WT, H221F and R312L |
| `fourha_mutation/` | HA complexes, WT and H221F |
| `N136D/` | N136D mutant with alginate substrates (MMMM, MMGG, MGMG) |
| top level | Trajectory alignment, pKa parsing, and Slurm job scripts |

Each system folder contains:

- **MD setup and run:** GROMACS `.mdp` parameter files and Slurm (`.sb`/`.sh`) job scripts
- **Structural analysis:** `rmsd.py`, `rmsd_docked.py`, `RMSF.py`, `fluctuations.py`, `aligned_trajectory.py`
- **Interaction analysis:** `h_bond.py`, `salt_bridge(s).py`, `protein_ligand_contact.py`, `ligand_molecules_contact.py`, `energy.py`
- **Conformational clustering:** `clustering.py`, `clustering_kmeans.py`, `clustering_GMVAE.py` (with `backend_GMVAE/`), `cluster_occurence.py`
- **Scoring:** `scoring_function.py`, `scoring_function_discrete.py`
- **Notebooks:** `analysis.ipynb`, `clustering.ipynb`
- **Environments:** conda `.yml` files

Trajectories and large data files are not included because of their size.

## Citation

If you use this code, please cite the manuscript linked above.
