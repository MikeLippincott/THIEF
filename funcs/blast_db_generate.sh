#!/bin/bash
#SBATCH --job-name=Blast_DB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=168:00:00
#SBATCH --mem=16gb
#SBATCH --output=BlastDB.%J.out
#SBATCH --error=BlastDB.%J.err

module load blast/2.10.0



makeblastdb -in CB4856.fna  -dbtype nucl -out CB4856/db_CB4856
