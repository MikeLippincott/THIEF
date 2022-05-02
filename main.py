import argparse
import subprocess

parser = argparse.ArgumentParser()

parser.add_argument('-pl', '--Lpath',  help="Path containing L arm fastas", type=str)
parser.add_argument('-pr', '--Rpath', help="Path containing R arm fastas",type=str)
parser.add_argument('-of', '--out_file', help="name of output file (no extension)",type=str)
parser.add_argument('-t', '--telo_seq', help="telomere sequence e.g. 'ttaggg' ",type=str)
parser.add_argument('-g', '--gnbk_file', help="Path to ape file for fasta conversion",type=str)
# args = parser.parse_known_args()



# parser.add_argument('-p',"--param1", help="First  Number for Operation",type=str)
# parser.add_argument("param2", help="Second Number for Operation")
# parser.add_argument("--power-to", help="Raise Addition of Parameters to the Power", type=int)

args = parser.parse_args()

print(args.Lpath)
print(args.Rpath)
print(args.out_file)
print(args.telo_seq)
print(args.gnbk_file)

LPATH = args.Lpath
RPATH = args.Rpath
OUT_FILE = args.out_file
TELO_SEQ = args.telo_seq
GNBK = args.gnbk_file

"""
Setup
gnbk2fasta # provide as an option
Thief
Filter.R
csv2fasta
blast scripts
"""

# set_up_dirs()
if not GNBK is None:
    gnbk2fasta(GNBK)

thief_call(LPATH, RPATH , OUT_FILE, TELO_SEQ)
subprocess.call(f'Rscript Filter.R -f {} -r {}", shell=True)


# set_up_dirs(PATH)
# gnbk2fasta(path_n_gnbkfile)
# thief_call(path1, strand1, path2, strand2, out_path, out_file_name, out_file_extension, telo_seq)
# Filter.R
# thief_csv2fasta(path)
# blast_db_generate.sh
# blast_query.sh
# run_blast2bed.sh (blast2bed.sh)
# blast_column_names.R



# subprocess.call("Rscript testScript.R -f test1 -r test2", shell=True)


