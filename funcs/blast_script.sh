#!/bin/bash

while getopts g:f: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    f) input_fasta=${OPTARG};;
  esac
done

wd=`pwd`
wd="/Users/mike/OneDrive\ -\ Maryville\ University/github/THIEF"

genome_name="${genome}"
genome="${genome}.fna"
genome_path="${wd}/Input_Files/Genomes/${genome}"
blast_db_out="${wd}/Output_Files/Blast_results/${genome_name}/db_${genome_name}"

echo ${genome_name}
echo ${genome}
echo ${genome_path}
echo ${blast_db_out}
echo ${wd}





makeblastdb -in "/Users/mike/OneDrive\ -\ Maryville\ University/github/THIEF/Input_Files/Genomes/CB4856.fna" -dbtype nucl -out "/Users/mike/OneDrive\ -\ Maryville\ University/github/THIEF/Output_Files/Blast_results/CB4856/db_CB4856"

#OUTFMT="6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq"
#blast_file_out="Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt"





#cp ${genome_path} Output_Files/Blast_results/${genome_name}/${genome}
#
#makeblastdb -in ${genome_path} -dbtype nucl -out ${blast_db_out} -title ${genome_name}
#
#OUTFMT="6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq"
#blast_file_out="Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt"

#blastn -query ${input_fasta} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt ${OUTFMT} -out ${blast_file_out}

#bash funcs/blast2bed.sh Blast_results/${genome_name}_blastn.txt


