import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-o', '--output', required=True,
                    help="shows output")

args = parser.parse_args()

if args.output:
    print(f'{args.output}')

"""
Setup
gnbk2fasta
Thief
Filter.R
csv2fasta
blast scripts
"""

from Setup import set_up_dirs
set_up_dirs('/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/THIEF_Dir')


# gnbk2fasta(path_n_gnbkfile)
#
# thief_csv2fasta(path)

main(path1, strand1, path2, strand2, out_path, out_file_name, out_file_extension, telo_seq)

