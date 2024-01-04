#!/bin/bash  
#SBATCH -o slurm.%j.%N.out  
#SBATCH --partition=compute
#SBATCH -J PCL-G16
#SBATCH -N 1
#SBATCH --ntasks-per-node=36
#SBATCH --get-user-env

g16 <Linux-A1.gjf> Linux-A1.out
