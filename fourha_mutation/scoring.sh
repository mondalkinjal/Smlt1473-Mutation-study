#!/usr/bin/env bash
#SBATCH --job-name=pytorch-gpu-shared
#### Change account below
#SBATCH --account=mda123
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=10G
#SBATCH --time=12:00:00
#SBATCH --output=pytorch-gpu-shared.o%j.%N

. "/home/kinjal14/scratch.energybio/miniconda/etc/profile.d/conda.sh"


conda init bash
conda activate DL
export OMP_NUM_THREADS=2
python -u scoring_function.py

#declare -xr SINGUALRITY_MODULE='singularitypro/3.9'

#module purge
#module load "${SINGUALRITY_MODULE}"
#module list
#printenv

#### We will run from the scratch directory local to the node
#cd /scratch/$USER/job_$SLURM_JOBID

#time -p singularity exec --bind /expanse,/scratch --nv /cm/shared/apps/containers/singularity/pytorch/pytorch-latest.sif python3 $SLURM_SUBMIT_DIR/clustering_gpu.py

#### List scratch directory
#ls /scratch/$USER/job_$SLURM_JOBID
