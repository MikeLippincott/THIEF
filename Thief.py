from Bio.Seq import Seq
import pandas as pd
import numpy as np
import os
from datetime import datetime

"Welcome to the Telomere Homology Imperfection Elucidation Function (THIEF) Script"


class Thief:

    def __init__(self, file, strand='f', telomere_sequence='ttaggc'):
        self.file = file
        self.strand = strand
        self.seek = telomere_sequence
        #self.seek = 'GCCTAA'
        self.frame_size = len(self.seek)
        self.tmp = ''

    def read_fasta(self, fp):
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
#
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
                    self.tmp += '_'
                #print('TRUE')
            else:
                #print('FALSE')
                #print(self.f[:1])
                self.tmp += f[:1]
                i+=1

    def data_compile(self, filename):

        filename = filename.split('>')[1]
        index = []
        for i in range(len(self.tmp)):
            index.append(i)
        test = self.tmp.split('______')
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

    def run_theif(self):
        self.fasta_info(self.file)
        self.sliding_window(self.seq, self.frame_size, self.seek)
        self.data_compile(self.filename)


# Execute
class Run_all():

    def __init__(self, strand1='f', strand2='f',telomere_sequence='ttaggc'):
        self.strand1 = strand1
        self.strand2 = strand2
        self.seek = telomere_sequence

    def Chroms(self, path, strand):
        finaldf = pd.DataFrame(columns=['chrom', 'pos', 'seq', 'Telo', 'Length'])
        paths = [f.path for f in os.scandir(path) if f.is_file()]
        for i in paths:
            if i.endswith('.fasta'):
                theif = Thief(i, strand, self.seek)
                theif.run_theif()
                finaldf = pd.concat((finaldf, theif.df))
        self.finaldf = finaldf

    def combine_frames(self, path1, path2, outpath_file):
        self.Chroms(path1, self.strand1)
        self.all_frames = self.finaldf
        self.Chroms(path2, self.strand2)
        self.all_frames = pd.concat([self.all_frames,self.finaldf])
        self.all_frames.to_csv(outpath_file)


def main(path1, strand1, path2, strand2, out_path, out_file_name, out_file_extension, telo_seq):
    run_thief = Run_all(strand1,strand2, telo_seq)
    now = datetime.now()
    time = now.strftime("%Y_%m_%d__%H_%M")
    if not out_path.endswith('/'):
        output_path = out_path + '/'
    if not out_file_extension.startswith('.'):
        out_file_extension = '.' + out_file_extension
    out = f'{out_path}{time}_{out_file_name}{out_file_extension}'
    run_thief.combine_frames(path1, path2, out)

# Humans
if __name__ == "__main__":
    main('/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/Human/L/',
         'r',
         '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/Human/R/',
         'f',
         '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/Human/THIEF_output/',
         'Thief_Human_output',
         '.csv',
         'ttaggg')

# Worms
# if __name__ == "__main__":
#     main('/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/'\
#     'elegans igv/telo_fastas/L/WB235/',
#          'r',
#          '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/'\
#          'elegans igv/telo_fastas/R/WB235/',
#          'f',
#          '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/'\
#          'elegans igv/telo_fastas/THIEF_output/',
#          'WB235_Thief_C-elegans_output',
#          '.csv',
#          'ttaggc')
