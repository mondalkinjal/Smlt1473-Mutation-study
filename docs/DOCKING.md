# Rosetta molecular docking reference

For molecular docking, follow the official [Rosetta ligand-docking tutorial](https://docs.rosettacommons.org/demos/latest/tutorials/ligand_docking/ligand_docking_tutorial), as requested by the study author. The tutorial provides its own example scripts and input files; the original Smlt1473-specific docking scripts, flags and protocol XML files could not be recovered.

## Tutorial and execution location

Use a Linux workstation or HPC node with Rosetta installed and its database available. Work in a copy of the tutorial inputs, following its protein preparation, ligand preparation, and docking steps. The tutorial files belong under `demos/tutorials/ligand_docking/` in a complete Rosetta distribution; the copy at that path in the inspected SHELL archive is empty.

The tutorial uses a RosettaScripts XML protocol and an `options` file. After completing its input preparation, run the RosettaScripts executable with `@options` from the tutorial working directory. Select the executable name and location from your own Rosetta build. The tutorial explains model and score-file inspection. Its supplied receptor/ligand example is a teaching system, not Smlt1473.

Additional official references:

- [Preparing ligands](https://docs.rosettacommons.org/docs/latest/rosetta_basics/preparation/preparing-ligands): ligand parameter files and conformer preparation.
- [Working with glycans](https://docs.rosettacommons.org/docs/latest/application_documentation/carbohydrates/WorkingWithGlycans): carbohydrate representation and modeling tools relevant to HA and ManA substrates.
- [GlycanDock](https://docs.rosettacommons.org/docs/latest/application_documentation/carbohydrates/GlycanDock): an available protein–glycoligand docking method. This is an additional reference, not a claim that the archived study used this application. Its documented search is local around the initial glycan position.

For a new Smlt1473 docking calculation, prepare the intended WT or mutant receptor and substrate, verify sugar identities, glycosidic connectivity and protonation, and record the chosen protocol, parameters, version and pose-selection criteria. The tutorial settings cannot be assumed to reproduce the paper's original docking poses.

## Recovery status (2026-11-18)

Five Rosetta installation trees in SHELL were inspected. In the shared user archive, `rosetta/rosetta_src_2021.16.61629_bundle/main/demos/tutorials/` contains empty directories named `ligand_fourha`, `ligand_fourha_H221F`, `ligand_hexamana`, `ligand_hexamana_H221F`, and `ligand_hexamana_R312L`, among others. The author confirmed that no backup is available.

A scan of 15,100 candidate script/configuration paths across those trees found no file content matching the searched study identifiers (`Smlt1473`, `hexamana`, `tetraha`, `fourha`, `H221F`, `R312L`, `N136D`, or `biochemistry_mutation`). The inspected custom docking shell jobs refer to antibody/NB runs; they were not assigned to this paper. This search is evidence of the recovery gap, not proof that every possible file on the filesystem was examined.

The MD source and configuration archive is preserved separately in this repository. Rosetta itself, its database, vendor tutorial source and docking decoy collections are not redistributed here; use the official Rosetta resources above.
