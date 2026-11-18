#!/bin/bash
#SBATCH --job-name=dissociation
#SBATCH -A energybio-eng
#SBATCH -t 96:00:00
#SBATCH -n 96

module load gromacs

mpirun gmx_mpi mdrun -cpi step5_production.cpt -s step5_production.tpr -deffnm step5_production
