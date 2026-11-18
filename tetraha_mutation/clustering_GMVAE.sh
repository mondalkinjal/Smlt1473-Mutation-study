#!/usr/bin/env bash
#SBATCH --job-name=pytorch-gpu-shared
#### Change account below
#SBATCH --account=mda123
#SBATCH --partition=gpu-debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=90G
#SBATCH --gpus=1
#SBATCH --time=00:30:00
#SBATCH --output=pytorch-gpu-shared.o%j.%N


#declare -xr SINGUALRITY_MODULE='singularitypro/3.9'

#module purge
#module load "${SINGUALRITY_MODULE}"
#module list
#printenv

#### We will run from the scratch directory local to the node
#cd /scratch/$USER/job_$SLURM_JOBID

#time -p singularity exec --bind /expanse,/scratch --nv /cm/shared/apps/containers/singularity/pytorch/pytorch-1.12.1-ubuntu-20.04-cuda-11.2-mlnx-ofed-4.9-4.1.7.0-openmpi-4.1.3-20221009.sif python3 $SLURM_SUBMIT_DIR/clustering_GMVAE.py

#### List scratch directory
#ls /scratch/$USER/job_$SLURM_JOBID
. "/home/kmondal/miniconda3/etc/profile.d/conda.sh"
conda activate DL
export OMP_NUM_THREADS=2
python3 clustering_GMVAE.py
