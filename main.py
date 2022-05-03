import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-pl', '--Lpath',  help="Path containing L arm fastas", type=str)
parser.add_argument('-pr', '--Rpath', help="Path containing R arm fastas",type=str)
# parser.add_argument('-of', '--out_file', help="name of output file (no extension)",type=str)
parser.add_argument('-t', '--telo_seq', help="telomere sequence e.g. 'ttaggg' ",type=str)
parser.add_argument('-e', '--genome', help="Genome File for BLAST analysis", type=str)
# args = parser.parse_known_args()



# parser.add_argument('-p',"--param1", help="First  Number for Operation",type=str)
# parser.add_argument("param2", help="Second Number for Operation")
# parser.add_argument("--power-to", help="Raise Addition of Parameters to the Power", type=int)

args = parser.parse_args()

print(args.Lpath)
print(args.Rpath)
print(args.out_file)
print(args.telo_seq)
print(args.genome)

LPATH = args.Lpath
RPATH = args.Rpath
OUT_FILE = args.out_file
TELO_SEQ = args.telo_seq
if TELO_SEQ == 'ttaggc':
    ORGANISM == 'worms'
elif TELO_SEQ == 'ttaggg':
    ORGANISM == 'human'
else:
    ORGANISM == 'unknown'
GENOME_NAME= (args.genome).replace('.fna','')
GENOME = args.genome

"""
Setup
Thief
Filter.R
csv2fasta
blast scripts
"""

# THIEF structure
lst = ['Input_Files/',
       'Input_Files/Genomes/',
       'Input_Files/fasta/',
       'Input_Files/fasta/L/',
       'Input_Files/fasta/R/',
       'Output_files/',
       'Output_files/csv/',
       'Output_files/Blast_results/',
       f'Output_files/Blast_results/{GENOME_NAME}',
       f'Input_Files/fasta/L/{GENOME_NAME}',
       f'Input_Files/fasta/R/{GENOME_NAME}',
       f'Output_files/csv/{GENOME_NAME}']
for i in lst:
    set_up_dirs(i)




thief = Thief()
thief(LPATH, RPATH ,GENOME_NAME, ORGANISM, TELO_SEQ)

sub = subprocess.call(f'Rscript Filter.R -f {call.out} -r {ORGANISM}', shell=True)
def parse_stdout(sub_proc):
    lst = str(sub_proc).split('stdout=b\'[1] ')[1].split('[1]')
    print(str(lst[0]).strip('\\n').strip('"'))
    tmp_file = str(lst[1]).strip("\\n\')").strip('"').strip(' "')
blast_file = parse_stdout(sub)
thief_csv2fasta(blast_file)
fasta4blast = blast_file.replace('.csv','.fasta')

subprocess.call(f'blast_no_cluster.sh -g {GENOME_NAME} -f {fasta4blast}', shell=True)
blast_output = f'{GENOME_NAME}_blastn.txt'

subprocess.call(f'Rscript blast_column_names.R -f {blast_output}', shell=True)







# set_up_dirs(PATH)
# gnbk2fasta(path_n_gnbkfile)
# thief_call(path1, strand1, path2, strand2, out_path, out_file_name, out_file_extension, telo_seq)
# Filter.R
# thief_csv2fasta(path)
# blast_db_generate.sh
# blast_query.sh
# run_blast2bed.sh (blast2bed.sh)
# blast_column_names.R


