import argparse
import subprocess
import time
from subprocess import call
from subprocess import run
from funcs.setup import set_up_dirs
from funcs.thief import Thief
from funcs.csv2fasta import thief_csv2fasta


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

print(args.Lpath)
print(args.Rpath)
print(args.telo_seq)
print(args.genome)

LPATH = args.Lpath
RPATH = args.Rpath

TELO_SEQ = args.telo_seq
if TELO_SEQ == 'ttaggc':
    ORGANISM = 'worms'
elif TELO_SEQ == 'ttaggg':
    ORGANISM = 'human'
else:
    ORGANISM = 'unknown'
GENOME_NAME = (args.genome).replace('.fna','')
GENOME = args.genome

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
time.sleep(10)
a = sub_proc.communicate()
blast_file = str(a).split('[1]')[2].strip("', None)").strip('\\').strip('"')


thief_csv2fasta(blast_file)
fasta4blast = blast_file.replace('.csv','.fasta')
print(fasta4blast)

subprocess.run([f'bash funcs/blast_script.sh -g {GENOME_NAME} -f {fasta4blast}'], shell=True)
blast_output = f'Output_Files/Blast_results/{GENOME_NAME}/{GENOME_NAME}_blastn.txt'

subprocess.call(f'Rscript funcs/blast_column_names.R -f {blast_output}', shell=True)







# set_up_dirs(PATH)
# gnbk2fasta(path_n_gnbkfile)
# thief_call(path1, strand1, path2, strand2, out_path, out_file_name, out_file_extension, telo_seq)
# Filter.R
# thief_csv2fasta(path)
# blast_db_generate.sh
# blast_query.sh
# run_blast2bed.sh (blast2bed.sh)
# blast_column_names.R



# #
# file_path = 'Output_files/csv/CB4856/2022_05_03__16_00_THIEF_CB4856_wormsoutput.csv'
#
# sub_proc = subprocess.Popen([f'Rscript funcs/Filter.R -f {file_path} -r worms'],shell=True, stdout=subprocess.PIPE)
# time.sleep(10)
# a = sub_proc.communicate()
#
# print(str(a).split('[1]')[1].strip('\\n').strip(' "'))
# print(str(a).split('[1]')[2].strip("', None)").strip('\\').strip('"'))
#
#


