import argparse
import subprocess
import time
from subprocess import call
from subprocess import run
from setup import set_up_dirs
from thief import Thief
from csv2fasta import thief_csv2fasta


GENOME_NAME = None

parser = argparse.ArgumentParser()
parser.add_argument('-pl', '--Lpath',  help="Path containing L arm fastas", type=str)
parser.add_argument('-pr', '--Rpath', help="Path containing R arm fastas",type=str)
parser.add_argument('-t', '--telo_seq', help="telomere sequence e.g. 'ttaggg' ",type=str)
parser.add_argument('-g', '--genome', help="Genome File for BLAST analysis", type=str)
# args = parser.parse_known_args()



# parser.add_argument('-p',"--param1", help="First  Number for Operation",type=str)
# parser.add_argument("param2", help="Second Number for Operation")
# parser.add_argument("--power-to", help="Raise Addition of Parameters to the Power", type=int)

args = parser.parse_args()


LPATH = args.Lpath
RPATH = args.Rpath

TELO_SEQ = args.telo_seq
if TELO_SEQ == 'ttaggc':
    ORGANISM = 'worms'
elif TELO_SEQ == 'ttaggg':
    ORGANISM = 'human'
else:
    ORGANISM = 'unknown'

if (args.genome).endswith('.fna'):
    GENOME_NAME = (args.genome).replace('.fna','')
    GENOME = args.genome
elif(args.genome).endswith('.fa'):
    GENOME_NAME = (args.genome).replace('.fa','')
    GENOME = args.genome
else:
    print('check file extension')

"""
Setup
Thief
Filter.R
csv2fasta
blast scripts
"""


# THIEF structure
if GENOME_NAME is None:
    lst = ['Input_Files/',
           'Input_Files/Genomes/',
           'Input_Files/Fasta/',
           'Input_Files/Fasta/L/',
           'Input_Files/Fasta/R/',
           'Output_Files/',
           'Output_Files/csv/',
           'Output_Files/Blast_results/']
else:
    lst = [f'Output_Files/Blast_results/{GENOME_NAME}',
           f'Output_Files/Blast_results/{GENOME_NAME}/db_{GENOME_NAME}',
           f'Input_Files/Fasta/L/{GENOME_NAME}',
           f'Input_Files/Fasta/R/{GENOME_NAME}',
           f'Output_Files/csv/{GENOME_NAME}']
for i in lst:
    set_up_dirs(i)




thief = Thief(LPATH, RPATH ,GENOME_NAME, ORGANISM, TELO_SEQ)
thief.run_thief()
print(thief.out)


sub_proc = subprocess.Popen([f'Rscript funcs/Filter.R -f {thief.out} -r {ORGANISM}'],shell=True, stdout=subprocess.PIPE)
time.sleep(5)
a = sub_proc.communicate()

blast_file = f'{(thief.out).replace(".csv","")}_table_for_blast.csv'

thief_csv2fasta(blast_file)
fasta4blast = blast_file.replace('.csv','.fasta')

subprocess.run([f'bash funcs/blast_script.sh -g {GENOME_NAME} -f {fasta4blast}'], shell=True)
blast_output = f'Output_Files/Blast_results/{GENOME_NAME}/{GENOME_NAME}_blastn.txt'

subprocess.call(f'Rscript funcs/blast_column_names.R -f {blast_output}', shell=True)




