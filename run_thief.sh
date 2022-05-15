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
    py_out=$(python funcs/main.py -pl ${pl} -pr ${pr} -s ${teloseq} -g ${genome})
    echo $py_out
  elif [[ $file == *.fa ]]; then
    genome="$(basename "$file")" # basename with extension
    genome_name="$(basename "$file" .fa)" # basename with no extension
    pl="Input_Files/Fasta/L/${genome_name}/" # L dir
    pr="Input_Files/Fasta/R/${genome_name}/" # R dir
    echo $genome
    echo $genome_name
    echo $pl
    echo $pr
    py_out=$(python funcs/main.py -pl ${pl} -pr ${pr} -s ${teloseq} -g ${genome})
    echo $py_out
  else
    echo 'Check File Extension'
  fi
done


echo "Complete"


