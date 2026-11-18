# Code availability audit

Checked on **2026-11-18**.

## Verified MD archive

All **770 original code and configuration files** in this release match the SHELL `biochemistry_mutation` archive byte for byte. All **771 baseline GitHub files**, including the original README, matched local contents and executable modes before this documentation update. No original source or configuration file was changed.

The archive comparison found one extra `.sh` file: a third-party Miniconda installer. It is not research code and is not redistributed. Counts, per-file hashes, and detailed checks are in [code-audit.json](code-audit.json); every original source path is linked in the [complete index](CODE_INDEX.md).

From the repository root, verify the original sources with:

```bash
sha256sum -c SOURCE_SHA256SUMS
```

The manifest covers 770 original source/configuration files. It excludes the updated README and the newly added documentation.

## Rosetta docking

The original study-specific docking files are unavailable. Relevant named directories in SHELL are empty, and the author confirmed there is no backup. At the author's request, the [docking guide](DOCKING.md) refers readers to official Rosetta molecular-docking tutorials. These references do not establish the original study settings or reproduce its exact poses.

## Static checks

- Python syntax: 334 of 335 `.py` files parsed under Python 3.11.
- Notebook structure: all 49 `.ipynb` files were valid JSON with a cells array; cells were not executed.
- Shell syntax: `bash -n` checked all 149 `.sh`/`.sb` files; 21 reported syntax errors.

The unfinished Python duplicate is [fourha_mutation/fourha/H123/gromacs/python_files/salt_bridges.py](../fourha_mutation/fourha/H123/gromacs/python_files/salt_bridges.py) (syntax error at line 46, with additional incomplete code). The sibling [fourha_mutation/fourha/H123/gromacs/salt_bridges.py](../fourha_mutation/fourha/H123/gromacs/salt_bridges.py) parses, but has not been validated on the simulation data during this audit. Both originals are retained.

Shell files reporting syntax errors:

- [N136D/N136D_MGMG/h_130/gromacs/reduced.sb](../N136D/N136D_MGMG/h_130/gromacs/reduced.sb)
- [N136D/N136D_MGMG/noh_130/gromacs/reduced.sb](../N136D/N136D_MGMG/noh_130/gromacs/reduced.sb)
- [N136D/N136D_MMGG/h_130/gromacs/reduced.sb](../N136D/N136D_MMGG/h_130/gromacs/reduced.sb)
- [N136D/N136D_MMGG/noh_130/gromacs/reduced.sb](../N136D/N136D_MMGG/noh_130/gromacs/reduced.sb)
- [N136D/N136D_MMMM/h_130/gromacs/reduced.sb](../N136D/N136D_MMMM/h_130/gromacs/reduced.sb)
- [N136D/N136D_MMMM/noh_130/gromacs/reduced.sb](../N136D/N136D_MMMM/noh_130/gromacs/reduced.sb)
- [aligned_total.sb](../aligned_total.sb)
- [fourha_mutation/H221F_fourha/H123/gromacs/reduced.sb](../fourha_mutation/H221F_fourha/H123/gromacs/reduced.sb)
- [fourha_mutation/H221F_fourha/NOH123/gromacs/reduced.sb](../fourha_mutation/H221F_fourha/NOH123/gromacs/reduced.sb)
- [fourha_mutation/fourha/NOH123/gromacs/reduced.sb](../fourha_mutation/fourha/NOH123/gromacs/reduced.sb)
- [hexamana_mutation/H221F_hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/H221F_hexamana/H109/gromacs/reduced.sb)
- [hexamana_mutation/H221F_hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/H221F_hexamana/NOH109/gromacs/reduced.sb)
- [hexamana_mutation/R312L_hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/R312L_hexamana/H109/gromacs/reduced.sb)
- [hexamana_mutation/R312L_hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/R312L_hexamana/NOH109/gromacs/reduced.sb)
- [hexamana_mutation/hexamana/H109/gromacs/reduced.sb](../hexamana_mutation/hexamana/H109/gromacs/reduced.sb)
- [hexamana_mutation/hexamana/NOH109/gromacs/reduced.sb](../hexamana_mutation/hexamana/NOH109/gromacs/reduced.sb)
- [reduced.sb](../reduced.sb)
- [tetraha_mutation/H221F_tetraha/H123/gromacs/reduced.sb](../tetraha_mutation/H221F_tetraha/H123/gromacs/reduced.sb)
- [tetraha_mutation/H221F_tetraha/NOH123/gromacs/reduced.sb](../tetraha_mutation/H221F_tetraha/NOH123/gromacs/reduced.sb)
- [tetraha_mutation/tetraha/H123/gromacs/reduced.sb](../tetraha_mutation/tetraha/H123/gromacs/reduced.sb)
- [tetraha_mutation/tetraha/NOH123/gromacs/reduced.sb](../tetraha_mutation/tetraha/NOH123/gromacs/reduced.sb)

## Practical limits

Source completeness is established for the inspected MD archive, not for every computation reported in the paper. Trajectories, complete topologies/force-field inputs, reference structures, clustering outputs and historical environments are not all supplied. Some scripts contain historical absolute paths, fixed frame counts, and data-specific selections. Syntax checks do not establish numerical correctness or end-to-end reproducibility. No simulation, docking, or paper-figure reproduction was performed.

Use the [analysis guide](ANALYSIS_GUIDE.md) for execution context and the [paper](https://pubs.acs.org/doi/10.1021/acs.jpcb.4c08753) for the published scientific methods.
