#!/bin/bash

###
#SBATCH --job-name=plinkprune
#SBATCH --output=/scratch/c.c1928239/new_builds/outputs/prune_%J.o
#SBATCH --error=/scratch/c.c1928239/new_builds/outputs/prune_%J.e
#SBATCH --time=3-00:00
#SBATCH --account=scw1452
#SBATCH --partition=c_compute_neuro1
#SBATCH --mem=100G
#SBATCH --ntasks=40
#SBATCH --tasks-per-node=40
#SBATCH --array=1-24%3
###

module load plink/1.9

cd /scratch/c.c1928239/new_builds/chr_${SLURM_ARRAY_TASK_ID}

# Run LD pruning in PLINK. This --indep command defines three parameters: window size (SNPs), n SNPs to shift the window at each step, and VIF threshold (1/(1-R^2), so R^2 here is 0.5.
plink --bfile PLINK_FILES_chr_${SLURM_ARRAY_TASK_ID} \
--indep 50 5 2 \
--out PLINK_FILES_chr_${SLURM_ARRAY_TASK_ID}_pruned
