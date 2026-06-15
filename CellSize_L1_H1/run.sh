#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=128
#SBATCH --time=20

module load lammps
module load openmpi

bash applystress.sh