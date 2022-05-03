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
        self.temp_string = ''

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

    def data_concatenation(self):
        path_lst = [self.lpath, self.rpath]
        finaldf = pd.DataFrame(columns=['chrom', 'pos', 'seq', 'Telo', 'Length'])
        for i in path_lst:
            paths = [f.path for f in os.scandir(i) if f.is_file()]
            for i in paths:
                if i.endswith('.fasta'):
                    if i == self.lpath:
                        self.strand = 'r'
                        self.fasta_info(self.file)
                    elif i == self.rpath:
                        self.strand = 'f'
                        self.fasta_info(self.file)
                    else:
                        print('Error: neither f or r were selected')
                    self.sliding_window(self.seq, self.frame_size, self.seek)
                    self.data_compile(self.filename)
                    finaldf = pd.concat((finaldf, self.df))
        self.all_frames = finaldf

    def wrap_up_file(self):
        OUT_PATH = f'Output_files/csv/{self.Genome_name}/'

        now = datetime.now()
        time = now.strftime("%Y_%m_%d__%H_%M")

        out_file_name = f'THIEF_{Genome_name}_{organism}output'

        OUT_FILE_EXTENSION = '.csv'

        self.out = f'{OUT_PATH}{time}_{out_file_name}{OUT_FILE_EXTENSION}'
        self.all_frames.to_csv(self.out)












