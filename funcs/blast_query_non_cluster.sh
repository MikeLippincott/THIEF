#!/bin/sh
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p general
#SBATCH -t 10:00:00
#SBATCH --mem-per-cpu=8g
#SBATCH --array=0-40
#SBATCH -o out_%A%.txt
#SBATCH -e err_%A%.txt

module load blast/2.10.0
# bash script for slurm blast
# CB4856
blastn -query 2022_04_28__11_36_CB4856_Thief_C-elegans_output_table_for_blast.fasta -db CB4856/db_CB4856
-evalue 1e-6 -num_threads 4 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out Blast_results/CB4856_blastn.txt




