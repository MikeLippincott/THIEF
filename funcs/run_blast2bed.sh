#!/bin/sh
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p general
#SBATCH -t 10:00:00
#SBATCH --mem-per-cpu=8g
#SBATCH --array=0-40
#SBATCH -o out_%A.txt
#SBATCH -e err_%A.txt


# run blast2bed script
bash blast2bed.sh Blast_results/CB4856_blastn.txt

