from Bio import SeqIO
import argparse
import os
import sys
path=os.getcwd()
sys.path.insert(0, f'{path}/')
from funcs.setup import set_up_dirs

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',  help="Path to genome file.fna", type=str)
parser.add_argument('-b', '--begin', help="begining of range (0)",type=int)
parser.add_argument('-e', '--end', help="end of slicing range (100000)",type=int)
parser.add_argument('-s', '--step_size', help="interval of telomere slicing", type=int)
parser.add_argument('-t', '--telo_seq', help="telomere seuqence to be added", type=str)
parser.add_argument('-x', '--extension', help="file extension", type=str)

args = parser.parse_args()

from funcs.setup import set_up_dirs

file = os.path.basename(args.input).replace(f'{arg.extension}',"")
import_path = f'Input_Files/Genomes/{args.input}'
set_up_dirs('Misc_funcs/Output/')
set_up_dirs('Misc_funcs/Output/Index')
set_up_dirs('Misc_funcs/Output/Blast/')
output_dir = f'Misc_funcs/Output/Index/{file}/'
set_up_dirs(output_dir)

class TeloFragment:

    def __init__(self, telo_sequence):
        self.telomere = telo_sequence
        self.telomere6 = telo_sequence*6

    def genome2dict(self, input_file_path):
        # input_file_path: path of file

        lst=[]
        lst1=[]
        path = os.path.dirname(input_file_path)
        self.genome_name = os.path.basename(input_file_path).replace(f'{arg.extension}','')
        if not path.endswith('/'):
            path = path + '/'
        for i in SeqIO.parse(f'{input_file_path}', 'fasta'):
            chrom = i.id
            print(chrom)
            seq = str(i.seq)
            lst.append(chrom)
            lst1.append(seq)
        self.mstr = dict((zip(lst,lst1)))

    # slices chromosome by defined interval for chromosomal telomere fragemnts. Output is a dict
    def telo_fragment_extract(self, Genome, arm, dictionary_of_seqs, start, end, step_size):
        dict = {}
        prior = 0
        for j in dictionary_of_seqs:
            for i in range(start, end, step_size):
                if arm == 'L':
                    L = dictionary_of_seqs[j][prior:i]
                    dict[(f'{j}_{arm}_{prior}..{i}_{Genome}_Fragment_Size-{step_size}')] = L
                    prior = i
                elif arm == 'R':
                    if i == 0:
                        R = dictionary_of_seqs[j][-prior:]
                        dict[(f'{j}_{arm}_{prior}..{i}_{Genome}_Fragment_Size-{step_size}')] = R
                        prior = i
                    else:
                        R = dictionary_of_seqs[j][-prior:-i]
                        dict[(f'{j}_{arm}_{prior}..{i}_{Genome}_Fragment_Size-{step_size}')] = R
                        prior = i
                else:
                    "Error Argument for 'Arm' should be 'L' or 'R'."
        dict["Telomere"] = self.telomere
        dict["Telomere6"] = self.telomere6
        self.dict = dict

    @staticmethod
    def file_write(dict, output_path):
        for i in (dict):
            filename = i
            if not output_path.endswith('/'):
                output_path = output_path + '/'
            ofile = open(f'{output_path}{i}', "w")
            #print(i)
            ofile.write(">" + i + "\n" + dict[i] + "\n")
            ofile.close()

    def run(self, input_file_path, arm, start, end, step_size, output_path):
        self.genome2dict(input_file_path)
        self.telo_fragment_extract(self.genome_name, arm, self.mstr, start, end, step_size)
        self.file_write(self.dict, output_path)


def main():
    for i in ('L', 'R'):
        telo = TeloFragment(args.telo_seq)
        telo.run(import_path, i, args.begin, args.end, args.step_size, output_dir)

if __name__ == "__main__":
    main()


