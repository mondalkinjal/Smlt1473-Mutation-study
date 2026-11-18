# Effect of Mutations on Smlt1473 Binding to Various Substrates Using Molecular Dynamics Simulations

Original code and simulation parameter files accompanying the manuscript:

> **Effect of Mutations on Smlt1473 Binding to Various Substrates Using Molecular Dynamics Simulations**
> *J. Phys. Chem. B* **2025**, 129 (16), 3948–3962.
> Manuscript: [https://pubs.acs.org/doi/10.1021/acs.jpcb.4c08753](https://pubs.acs.org/doi/10.1021/acs.jpcb.4c08753)

## Code, docking and running the analyses

- [Complete source index](docs/CODE_INDEX.md): links to all **770 original code and configuration files**.
- [Analysis and execution guide](docs/ANALYSIS_GUIDE.md): where to run the scripts, dependencies, input files, and analysis stages.
- [Rosetta molecular docking reference](docs/DOCKING.md): official tutorials for docking, as requested by the author. The original study-specific docking scripts and flags are unavailable.
- [Code availability audit](docs/CODE_AUDIT.md): archive/GitHub verification and known legacy syntax issues.
- [Source checksums](SOURCE_SHA256SUMS) and [machine-readable audit](docs/code-audit.json).

The 770 source/configuration files match the archived MD project byte for byte. They are preserved unchanged. Full trajectories and complete prepared simulation systems are not included, and the release audit did not rerun the calculations.

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
