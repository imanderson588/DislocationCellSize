#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=128
#SBATCH --time=20

module purge 

module load gnu13
module load openmpi
export PATH=$PATH:/home/C836791915/lammps_compute_PACE/build/

bash applystress.sh