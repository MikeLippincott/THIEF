#!/bin/bash

while getopts g:f: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    i) input_contig=${OPTARG};;
  esac
done


genome_name="${genome}"
genome="${genome}.fna"
genome_path="Input_Files/Genomes/${genome}"
input_contig_path="Input_Files/Genomes/Contig_Genomes/${input_contig}"
input_contig_name="$(basename "${input_contig}")"
blast_db_out="Misc_tools/Output/${input_contig_name}/db_${input_contig_name}/db_${input_contig_name}"

echo ${genome_name}
echo ${genome}
echo ${genome_path}


# slice the complete reference

python Misc_tools/telomere_slicer.py -i ${genome} -b 0 -e 100000 -s 10000 -t ttaggc

for file in Misc_tools/Output/${genome_name}/*; do
  exportfile="Misc_tools/Output/${genome_name}/${genome_name}.txt"
  cat ${file} >> ${exportfile} && rm ${file}
done




# dbb is made from contig assembly

makeblastdb -in ${input_contig_path} -dbtype nucl -out ${blast_db_out} -title ${input_contig_name}



blast_file_out="Misc_tools/Output/${input_contig_name}/${input_contig_name}_blastn.txt"


blastn -query ${genome_path} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out ${blast_file_out}



