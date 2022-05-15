#!/bin/bash

while getopts g:f: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    f) input_fasta=${OPTARG};;
  esac
done

echo $genome
if [[ ${genome} == *.fna ]]; then
  genome="$(basename "$genome")" # basename with extension
  genome_name="$(basename "$genome" .fna)" # basename with no extension
  genome_path="Input_Files/Genomes/${genome}"
  blast_db_out="Output_Files/Blast_results/${genome_name}/db_${genome_name}/db_${genome_name}"

  echo ${genome}
  echo ${genome_name}
  echo ${genome_path}
  echo ${blast_db_out}
elif [[ $genome == *.fa ]]; then
  genome="$(basename "$genome")" # basename with extension
  genome_name="$(basename "$genome" .fa)" # basename with no extension
  genome_path="Input_Files/Genomes/${genome}"
  blast_db_out="Output_Files/Blast_results/${genome_name}/db_${genome_name}/db_${genome_name}"

  echo ${genome}
  echo ${genome_name}
  echo ${genome_path}
  echo ${blast_db_out}
else
  echo "blast-script.sh error chekc inputs"
fi


makeblastdb -in ${genome_path} -dbtype nucl -out ${blast_db_out} -title ${genome_name}


blast_file_out_2bed="Output_Files/Blast_results/${genome_name}/${genome_name}_blast2bed.txt"
blast_file_out="Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt"


blastn -query ${input_fasta} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt 6 -out ${blast_file_out_2bed}
blastn -query ${input_fasta} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out ${blast_file_out}


bash funcs/blast2bed.sh ${blast_file_out_2bed}

