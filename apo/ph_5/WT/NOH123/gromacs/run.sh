#!/bin/bash
#SBATCH --job-name=dissociation
#SBATCH -A energybio-eng 
#SBATCH -t 120:00:00
#SBATCH -n 96

module load gromacs
#minimization
#export GMX_MAXCONSTRWARN=-1
gmx_mpi grompp -f step4.0_minimization.mdp -o step4.0_minimization.tpr -c step3_input.gro -r step3_input.gro -p topol.top -n index.ndx
mpirun gmx_mpi mdrun -deffnm step4.0_minimization
#unset GMX_MAXCONSTRWARN
#equilibration
gmx_mpi grompp -f step4.1_equilibration.mdp -o step4.1_equilibration.tpr -c step4.0_minimization.gro -r step4.0_minimization.gro -p topol.top -n index.ndx
# Run the equilibration
mpirun gmx_mpi mdrun -deffnm step4.1_equilibration
#production
gmx_mpi grompp -f step5_production.mdp -o step5_production.tpr -c step4.1_equilibration.gro -r step4.1_equilibration.gro -p topol.top -n index.ndx
mpirun gmx_mpi mdrun -deffnm step5_production

