#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=64
#SBATCH --time=5

module load lammps
module load openmpi

bash applystress.sh