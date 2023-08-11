#!/bin/bash

###
#SBATCH --job-name=UKB_analysis
#SBATCH --output=/scratch/c.c1928239/outputs/%J.o
#SBATCH --error=/scratch/c.c1928239/outputs/%J.e
#SBATCH --time=3-00:00
#SBATCH --account=scw1452
#SBATCH --partition=c_compute_neuro1
#SBATCH --mem=200G
#SBATCH --ntasks=40
#SBATCH --tasks-per-node=40
#SBATCH --array=1-24%3
###

# Set up modules required
module rm compiler/intel/2018/2 
module load ensembl-vep/102.0 
module load samtools/1.10
module load python/3.7.0
module load anaconda/2020.02
module load sqlite3/3270200
module load htslib/1.10.2

# Set up links to temporary directory with plenty of space 
export SPARK_WORKER_DIR=/scratch/c.c1928239/tmp/  
export SPARK_LOG_DIR=/scratch/c.c1928239/tmp/   
export SPARK_LOCAL_DIRS=/scratch/c.c1928239/tmp/
export LD_PRELOAD=/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3

# Navigate to correct chromosome and then run python hail script. Use slightly less memory in python than requested in bash script 
cd /scratch/c.c1928239/new_builds/chr_${SLURM_ARRAY_TASK_ID}
PYSPARK_SUBMIT_ARGS="--driver-java-options -Djava.io.tmpdir=/scratch/c.c1928239/tmp --driver-library-path /scratch/c.c1928239/tmp --driver-memory 190g --executor-memory 190g pyspark-shell" python3 /scratch/c.c1928239/new_builds/script.py ${SLURM_ARRAY_TASK_ID}