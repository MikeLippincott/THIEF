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



# args
while getopts s: flag
do
  case "${flag}" in
    s) teloseq=${OPTARG};;
  esac
done



file_dir='Input_Files/Genomes/*'
# loop through all files in dir
for file in $file_dir; do
  echo $file
  if [[ $file == *.fna ]]; then
    genome="$(basename "$file")" # basename with extension
    genome_name="$(basename "$file" .fna)" # basename with no extension
    pl="Input_Files/Fasta/L/${genome_name}/" # L dir
    pr="Input_Files/Fasta/R/${genome_name}/" # R dir
    echo $genome
    echo $genome_name
    echo $pl
    echo $pr
    thief_file=$(python funcs/call_thief.py -pl ${pl} -pr ${pr} -s ${teloseq} -g ${genome})
    echo $thief_file

    Rscript funcs/Filter.R -f $thief_file -s $teloseq

    blast_file=${thief_file/".csv"/"_table_for_blast.csv"/}
    echo $blast_file

    python csv2fasta.py -f $blast_file
    fasta4blast=${blast_file/".csv"/".fasta"/}

    bash funcs/blast_script.sh -g $genome -f $fasta4blast
    blast_output='Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt'
    Rscript funcs/blast_column_names.R -f $blast_output


  elif [[ $file == *.fa ]]; then
    genome="$(basename "$file")" # basename with extension
    genome_name="$(basename "$file" .fa)" # basename with no extension
    pl="Input_Files/Fasta/L/${genome_name}/" # L dir
    pr="Input_Files/Fasta/R/${genome_name}/" # R dir
    echo $genome
    echo $genome_name
    echo $pl
    echo $pr
    thief_file=$(python funcs/call_thief.py -pl ${pl} -pr ${pr} -s ${teloseq} -g ${genome})
    echo $thief_file

    Rscript funcs/Filter.R -f $thief_file -s $teloseq

    blast_file=${thief_file/".csv"/"_table_for_blast.csv"/}
    echo $blast_file

    python csv2fasta.py -f $blast_file
    fasta4blast=${blast_file/".csv"/".fasta"/}

    bash funcs/blast_script.sh -g $genome -f $fasta4blast
    blast_output='Output_Files/Blast_results/${genome_name}/${genome_name}_blastn.txt'
    Rscript funcs/blast_column_names.R -f $blast_output

  else
    echo 'Check File Extension'
  fi
done


echo "Complete"

