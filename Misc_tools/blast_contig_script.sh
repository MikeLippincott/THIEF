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
input_fasta_name="$(basename "${input_fasta}")"
blast_db_out="Misc_tools/Output/${input_fasta_name}/db_${input_fasta_name}/db_${input_fasta_name}"

echo ${genome_name}
echo ${genome}
echo ${genome_path}
echo ${blast_db_out}



makeblastdb -in ${input_fasta} -dbtype nucl -out ${blast_db_out} -title ${input_fasta_name}



blast_file_out="Misc_tools/Output/${input_fasta_name}/${input_fasta_name}_blastn.txt"


blastn -query ${genome_path} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out ${blast_file_out}



