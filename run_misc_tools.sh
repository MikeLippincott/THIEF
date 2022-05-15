#!/bin/bash
#SBATCH --job-name=run_thief
#SBATCH -t 1-23
#SBATCH --mem=16G
#SBATCH --output=out_%j.log
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=email@ufl.edu

module load python/3.8.8
module load r/4.1.3
module load blast/2.13.0

while getopts s: flag
do
  case "${flag}" in
    s) telo_seq=${OPTARG};;
  esac
done

REF_PATH="Input_Files/Genomes/*.fna"
for ref in $REF_PATH; do
        ref="$(basename "$ref" .fna)"
        for genome in Input_Files/Genomes/Contig_Genomes/*; do
                genome="$(basename "$genome" .fna)"
                bash Misc_funcs/Contig_blast.sh -g $ref -i $genome -s $telo_seq
        done
done