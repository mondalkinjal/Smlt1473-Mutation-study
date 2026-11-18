# Analysis and execution guide

The repository preserves the original scripts and parameters for the Smlt1473 mutation study. Run Python analysis on a Linux workstation or an HPC analysis node with the required scientific packages; submit Slurm scripts only on a matching HPC installation. GROMACS runs require a complete prepared simulation system. This is an archive with system-specific scripts, not an installed command-line application.

## Find the appropriate system

Use the [complete code index](CODE_INDEX.md) to find the scripts for the substrate, mutant, and protonation directory being analyzed. `apo/` contains pH 5 and pH 9 systems; `tetraha_mutation/`, `hexamana_mutation/`, `fourha_mutation/`, and `N136D/` preserve the historical complex directory names. Retaining a directory does not imply that every exploratory variant appears in the final paper.

## Inputs and environment

Restore the matching coordinates, topology and included force-field files, index groups, and trajectories before running the scripts. Examples of filenames expected by analyses are `protein_ligand.gro`, `final_production.xtc`, and `aligned.xtc`. Simulation jobs also expect prepared files such as `step3_input.gro`, `topol.top`, and `index.ndx`; production continuation jobs may need an existing `.tpr` or checkpoint. These data files are not supplied by this code release.

The Python sources import MDAnalysis, NumPy, pandas, SciPy, scikit-learn, PyTorch, Matplotlib, python-docx, and py3Dmol, in addition to standard-library modules and the included `backend_GMVAE` code. Different stages need different subsets. GROMACS/MPI, VMD and its interaction plugins, and Slurm/module settings are additional dependencies used by specific jobs. Historical exports such as [GNN.yml](../GNN.yml) are included for provenance; a fresh portable installation has not been validated.

Review absolute data paths, module names, account/partition requests, atom and residue selections, fixed box dimensions, and frame limits before running a script. Several scripts use 7,501-frame blocks and residue-number offsets such as `+21`; these must match the original input ordering and residue mapping.

## Workflow and representative entry points

The following links identify examples of each analysis. Use the corresponding variant in the directory for your system.

| Stage | Included example | Required context / result |
|---|---|---|
| Molecular docking | [Rosetta reference](DOCKING.md) | Official tutorials are linked; the original study-specific docking files are unavailable. |
| MD minimization, equilibration and production | [apo run.sh](../apo/ph_5/WT/H123/gromacs/run.sh), [complex production.sb](../tetraha_mutation/tetraha/H123/gromacs/production.sb) | Complete prepared system; `.mdp` files specify simulation settings. Check whether a job starts or continues production. |
| Trajectory alignment | [aligned_trajectory.py](../aligned_trajectory.py) | Matching `protein_ligand.gro` and `final_production.xtc`; writes aligned trajectory. |
| RMSD and docking-reference comparison | [rmsd.py](../tetraha_mutation/rmsd.py), [rmsd_docked.py](../fourha_mutation/rmsd_docked.py) | Matching structures, trajectories and reference structures. |
| RMSF and distance fluctuations | [RMSF.py](../tetraha_mutation/RMSF.py), [fluctuations.py](../tetraha_mutation/fluctuations.py) | System-specific trajectories, selections and mapping. |
| Hydrogen bonds | [h_bonds.tcl](../tetraha_mutation/tetraha/H123/gromacs/h_bonds.tcl), [important_hydrogen.py](../tetraha_mutation/tetraha/H123/gromacs/important_hydrogen.py), [h_bond.py](../tetraha_mutation/h_bond.py) | VMD trajectory analysis, per-residue interaction files, then Python summaries. |
| Salt bridges | [salt_bridge.tcl](../fourha_mutation/fourha/NOH123/gromacs/salt_bridge.tcl), [salt_bridges.py](../fourha_mutation/fourha/H123/gromacs/salt_bridges.py) | VMD/plugin output and system-specific residue numbering. Check Tcl contents: some historical filenames do not describe the plugin they call. |
| Protein–ligand and ligand contacts | [protein_ligand_contact.py](../tetraha_mutation/protein_ligand_contact.py), [ligand_molecules_contact.py](../tetraha_mutation/ligand_molecules_contact.py) | Trajectories, distance thresholds and selections. |
| K-means and GMVAE clustering | [clustering_kmeans.py](../tetraha_mutation/clustering_kmeans.py), [clustering_GMVAE.py](../tetraha_mutation/clustering_GMVAE.py), [backend_GMVAE.py](../tetraha_mutation/backend_GMVAE/backend_GMVAE.py) | Distance features across the intended systems and frame order. |
| Cluster occupancy/residence and interaction summaries | [cluster_occurence.py](../tetraha_mutation/cluster_occurence.py), [snapshot_indices.py](../tetraha_mutation/snapshot_indices.py) | Matching cluster-label arrays and, for interaction summaries, per-frame interaction data. |
| Protein–ligand interaction energies | [energy_combined.sb](../tetraha_mutation/tetraha/H123/gromacs/energy_combined.sb), [energy.py](../tetraha_mutation/energy.py) | GROMACS rerun and energy extraction, followed by summaries using cluster labels. |
| Clustering evaluation | [scoring_function.py](../tetraha_mutation/scoring_function.py), [scoring_function_discrete.py](../tetraha_mutation/scoring_function_discrete.py) | Cluster/structural/interaction metrics; these are not the Rosetta docking score function. |
| pKa tables | [read_extract_pka.py](../read_extract_pka.py), [apo parser](../apo/read_extract_pka.py) | Existing `.pka` outputs; the root parser writes `merged_pka_table.docx`. |
| Interactive analysis | [analysis.ipynb](../tetraha_mutation/analysis.ipynb), [clustering.ipynb](../tetraha_mutation/clustering.ipynb) | Notebook kernels need the same dependencies and original data paths. |

## Running an analysis

For a script that expects local input files, enter that system's working directory and run `python script_name.py` using its analysis environment. Scripts that call `os.chdir(...)` use their embedded paths instead; update those paths in a working copy first. Follow the inputs and outputs in the source when choosing execution order. For example, cluster summaries require labels, and cluster energies also require the GROMACS energy extraction output.

The representative tetraha clustering scripts save `cluster_KMeans.npy` and `clustering_GMVAE.npy`, while downstream scripts expect `labels_kmeans.npy` and `labels_GMVAE.npy`. Confirm the chosen clustering variant, frame count and concatenation order before explicitly providing the corresponding downstream label files. The archive does not automatically reconcile these historical names.

For Slurm, inspect the selected job and its input files, then submit it from the intended working directory with `sbatch job_name.sb` (or its `.sh` filename). Do not submit all archived jobs together: some are alternatives, reruns, or continuation jobs.

## Verification limits

The [audit](CODE_AUDIT.md) records one unfinished Python duplicate and 21 shell files with syntax errors. Source bytes were preserved. Parsing does not validate scientific results, GPU execution, external tools, or data availability. No simulations or paper figures were regenerated during this release audit.
