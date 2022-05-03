#!/bin/bash

while getopts g:f: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    f) input_fasta=${OPTARG};;
  esac
done

genome_name="${genome}"
genome="${genome}.fna"
genome_path="Input_Files/Genomes/${genome}"
blast_db_out="Output_Files/Blast_results/${genome_name}/db_${genome_name}"


cp ${genome_path} Output_Files/Blast_results/${genome_name}/${genome}
makeblastdb -in ${genome_path} -dbtype nucl -out ${blast_db_out}

OUTFMT="6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq"
blast_file_out="Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt"

#blastn -query ${input_fasta} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt ${OUTFMT} -out ${blast_file_out}

#bash funcs/blast2bed.sh Blast_results/${genome_name}_blastn.txt


