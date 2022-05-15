import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_path',  help="Path containing csv table for fasta", type=str)
args = parser.parse_args()

# Csv from THIEF -> fasta
def thief_csv2fasta(path_n_csv): #file and path
    # Extract filename
    print(path_n_csv)
    filename = os.path.basename(path_n_csv)
    print(filename)
    path = os.path.dirname(path_n_csv)
    print(path)
    basename = filename.replace('.csv','')
    print(basename)
    df = pd.read_csv(path_n_csv)
    vals = [(w, x, y, z) for w, x, y, z in
            zip(df['value'], df['sandwhich_seq'], df['sandwhich_seq_L'], df['sandwhich_seq_R'])]
    outfile = f'{path}/{basename}.fasta'
    outfile = open(f'{path}/{basename}.fasta','w')
    for i in enumerate(vals):
        outfile.write(f'>raw_sandwhich_{i[0]}\n')
        outfile.write(f'{vals[i[0]][0]}\n')
        outfile.write(f'>double_sandwhich_{i[0]}\n')
        outfile.write(f'{vals[i[0]][1]}\n')
        outfile.write(f'>left_sandwhich_{i[0]}\n')
        outfile.write(f'{vals[i[0]][2]}\n')
        outfile.write(f'>right_sandwhich_{i[0]}\n')
        outfile.write(f'{vals[i[0]][3]}\n')
    outfile.close()

def main():
    thief_csv2fasta(args.file_path)


if __name__ == "__main__":
    main()