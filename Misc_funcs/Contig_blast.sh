#!/bin/bash

while getopts g:i:s:e: flag
do
  case "${flag}" in
    g) genome=${OPTARG};;
    i) input_contig=${OPTARG};;
    s) telo_seq=${OPTARG};;
    e) extension=${OPTARG};;
  esac
done


genome_name="${genome}"
rm -r Misc_funcs/Output/Index/${genome_name}/
rm Misc_funcs/Output/${genome_name}.txt

genome="${genome}${extension}"
genome_path="Input_Files/Genomes/${genome}"
input_contig_path="Input_Files/Genomes/Contig_Genomes/${input_contig}${extension}"
input_contig_name="$(basename "${input_contig}")"
blast_db_out="Misc_funcs/Output/Blast/${input_contig_name}/db_${input_contig_name}/db_${input_contig_name}"

echo ${genome_name}
echo ${genome}
echo ${genome_path}


# slice the complete reference

python Misc_funcs/telomere_slicer.py -i ${genome} -b 0 -e 100000 -s 5000 -t ${telo_seq} -x ${extension}


for file in Misc_funcs/Output/Index/${genome_name}/*; do
  exportfile="Misc_funcs/Output/${genome_name}.txt"
  cat ${file} >> ${exportfile} && rm -f ${file}
done



# db is made from contig assembly

makeblastdb -in ${input_contig_path} -dbtype nucl -out ${blast_db_out} -title ${input_contig_name}



blast_file_out="Misc_funcs/Output/Blast/${input_contig_name}/${input_contig_name}_blastn.txt"


blastn -query ${genome_path} -db ${blast_db_out} -evalue 1e-6 -num_threads 4 -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qseq sseq" -out ${blast_file_out}



