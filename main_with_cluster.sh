#!/bin/bash
#SBATCH --job-name=Blast_DB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=168:00:00
#SBATCH --mem=16gb
#SBATCH --output=BlastDB.%J.out
#SBATCH --error=BlastDB.%J.err

module load python/3.9.6
module load blast/2.13.0



# loop through all files in dir
for file in Input_Files/Genomes/*; do
  if [[ "$file" == *.fasta ]]       #  this is the snag
    then
  genome="$(basename "$file")" # basename with extension
  genome_name="$(basename "$file" .fna)" # basename with no extension
  pl="Input_Files/Fasta/L/${genome_name}/" # L dir
  pr="Input_Files/Fasta/L/${genome_name}/" # R dir
done;

echo ${genome}
echo ${genome_name}
echo ${pl}
echo ${pr}


python3 main.py -pl ${pl} -pr ${pr} -t ttaggc -g ${genome}
