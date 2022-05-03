#!/bin/bash

#makeblastdb -in CB4856.fna  -dbtype nucl -out CB4856/db_CB4856

while getopts g:f: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    f) input_csv=${OPTARG};;
  esac
done
echo "$genome"
echo "$input_csv"
path="Blast_results/${genome}/db_${genome}"
echo $path

makeblastdb -in ${genome}.fna -dbtype nucl -out ${path}

OUTFMT="6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq"
blast_out="Blast_results/${genome}/${genome}_blastn.txt"

blastn -query ${input_csv} -db ${path} -evalue 1e-6 -num_threads 4 -outfmt ${OUTFMT} -out ${blast_out}

bash blast2bed.sh Blast_results/${genome}_blastn.txt


