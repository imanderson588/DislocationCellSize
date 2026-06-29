#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=128
#SBATCH --time=20

module purge 

module load lammps/2025-ace-snap-meam

bash applystress.sh