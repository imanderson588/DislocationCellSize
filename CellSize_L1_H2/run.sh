#!/bin/bash

#SBATCH --partition=all
#SBATCH --job-name=lammps_run
#SBATCH --ntasks=64
#SBATCH --time=5

module purge 

module load lammps/2025-ace-snap-meam

bash apply_stress.sh