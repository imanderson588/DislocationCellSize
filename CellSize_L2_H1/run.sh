#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=64
#SBATCH --time=5

module load gnu13
module load openmpi
export PATH=$PATH:/home/C836791915/lammps_compute_PACE/build/

bash apply_stress.sh