#!/bin/bash
#SBATCH --job-name=Blast_DB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=168:00:00
#SBATCH --mem=16gb
#SBATCH --output=BlastDB.%J.out
#SBATCH --error=BlastDB.%J.err

