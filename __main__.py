from funcs.setup import set_up_dirs
import subprocess


lst = ['Input_Files/',
       'Input_Files/Genomes/',
       'Input_Files/Fasta/',
       'Input_Files/Fasta/L/',
       'Input_Files/Fasta/R/',
       'Output_Files/',
       'Output_Files/csv/',
       'Output_Files/Blast_results/']

for i in lst:
    set_up_dirs(i)

subprocess.run("bash funcs/main_no_cluster.sh", shell=True)