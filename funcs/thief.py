from Bio.Seq import Seq
import pandas as pd
import numpy as np
import os
from datetime import datetime


class Thief:

    def __init__(self, lpath, rpath, Genome_name, organism, telo_seq='ttaggc'):
        self.lpath = lpath
        self.rpath = rpath
        self.Genome_name = Genome_name
        self.organism = organism
        self.seek = telo_seq
        self.frame_size = len(telo_seq)
        self.temp_string = ''

    @staticmethod
    def read_fasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

    def fasta_info(self, file):
        with open(file) as fp:
            if self.strand == 'f':
                for name, seq in self.read_fasta(fp):
                    self.filename = name
                    self.seq = str(Seq(seq).lower())
            elif self.strand == 'r':
                for name, seq in self.read_fasta(fp):
                    self.filename = name
                    self.seq = str(Seq(seq).lower().reverse_complement())
            else:
                print("Error: Please specify either 'f' or 'r' stand parameter.")

    def sliding_window(self, elements, window_size, search_sequence):

        if len(elements) <= window_size:
            return elements
        i = 0
        #while i in range(len(elements) - window_size + 1):
            #f = elements[i:i+window_size]
        while i in range(len(elements)):
            f = elements[i:i+window_size]
            if f == search_sequence:
                #print(f)
                #outseq+=f
                i+=window_size
                for j in range(window_size):
                    self.temp_string += '_'
                #print('TRUE')
            else:
                #print('FALSE')
                #print(self.f[:1])
                self.temp_string += f[:1]
                i+=1

    def data_compile(self, filename):

        filename = filename.split('>')[1]
        index = []
        for i in range(len(self.temp_string)):
            index.append(i)
        test = self.temp_string.split('______')
        j = 0
        pos = []
        chrom =[]
        for i in test:
            if i == '':
                j += 6
                pos.append(j)
                for k in range(6):
                    chrom.append(filename)
                #print(j)
            else:
                #print(len(i))
                j += len(i)
                pos.append(j)
                chrom.append(filename)
        self.df = pd.DataFrame(list(zip(chrom,pos,test)), columns
        = ['chrom','pos','seq'])
        self.df['Telo'] = np.where(self.df['seq']!='',self.df['seq'],self.seek)
        self.df['Length'] = self.df['seq'].str.len()

    def wrap_up_file(self):
        OUT_PATH = f'Output_files/csv/{self.Genome_name}/'

        now = datetime.now()
        time = now.strftime("%Y_%m_%d__%H_%M")

        out_file_name = f'THIEF_{self.Genome_name}_{self.organism}output'

        OUT_FILE_EXTENSION = '.csv'

        self.out = f'{OUT_PATH}{time}_{out_file_name}{OUT_FILE_EXTENSION}'
        self.all_frames.to_csv(self.out)

    # calls fasta_info method
    # calls sliding_window method
    # calls data compile method
    # calls wrap_up_files method
    def run_thief(self):
        path_lst = [self.lpath, self.rpath]
        finaldf = pd.DataFrame(columns=['chrom', 'pos', 'seq', 'Telo', 'Length'])
        for j in path_lst:
            paths = [f.path for f in os.scandir(j) if f.is_file()]
            for i in paths:                     # for loop calls fasta_info
                if i.endswith('.fasta'):
                    if j == self.lpath:
                        self.strand = 'r'
                        self.fasta_info(i)
                    elif j == self.rpath:
                        self.strand = 'f'
                        self.fasta_info(i)
                    else:
                        print('Error: neither f or r were selected')
                    self.sliding_window(self.seq, self.frame_size, self.seek)  # sliding window method
                    self.data_compile(self.filename)                           # data compile method
                    finaldf = pd.concat((finaldf, self.df))
        self.all_frames = finaldf
        self.wrap_up_file()


















