#!/bin/bash
#SBATCH --job-name=dissociation
#SBATCH -A energybio-eng
#SBATCH -t 20:00:00
#SBATCH -n 1

module load gromacs
gmx_mpi select -f step5_production.xtc -n index.ndx -on output.ndx <<EOF
0
EOF
gmx_mpi trjconv -f step5_production.xtc -n output.ndx -o final_production.xtc -pbc nojump
gmx_mpi editconf -f step3_input.gro -n output.ndx -o protein.gro
