#!/bin/bash  
#SBATCH -o slurm.%j.%N.out  
#SBATCH --partition=compute
#SBATCH -J PCL-G16
#SBATCH -N 1
#SBATCH --ntasks-per-node=32
#SBATCH --get-user-env

g16 <Linux-A2.gjf> Linux-A2.out
