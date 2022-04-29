import Bio
from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd
import argparse
import os


class Telo_fragment:

    def __init__(self, telo_sequence):
        self.telomere = telo_sequence
        self.telomere6 = telo_sequence*6

    def genome2dict(self,input_path,filename,format):
        lst=[]
        lst1=[]
        if not input_path.endswith('/'):
            input_path = input_path + '/'
        for i in SeqIO.parse(f'{input_path}{filename}',format):
            chrom = i.id
            print(chrom)
            seq = str(i.seq)
            lst.append(chrom)
            lst1.append(seq)
        self.mstr = dict((zip(lst,lst1)))

    # def interval_gen(self, min, max, step_size):
    #     self.interval = []
    #     for i in range(min,max,step_size):
    #         slice_set = [prior:i]
    #         self.interval.append(i)
        # for int in interval:
        # list_ranges("N2",lst,range_lst,int,mstr,N2_min,N2_max)


    # slices chromosome by defined interval for chromosomal telomere fragemnts. Output is a dict
    def telo_fragment_extract(self,Genome, arm, dictionary_of_seqs, start, end, step_size):
        dict = {}
        # input vars :
        # L_start = Left telomere start coordinate (e.g. 3000) (bp)
        # R_end = right telomere end coordinate (e.g. 20924180) (bp)
        # Chr_name = Chromosome Name (e.g. IL)
        # for i, j, chr in zip(start, end, chr_name):
        #     k = start[i]
        #     l = end[j]
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

    def file_write(self, dict, output_path):
        for i in (dict):
            filename = i
            if not output_path.endswith('/'):
                output_path = output_path + '/'
            ofile = open(f'{output_path}{i}', "w")
            #print(i)
            ofile.write(">" + i + "\n" + dict[i] + "\n")
            ofile.close()

    def run(self,input_path,filename,format,Genome, arm, start, end, step_size, output_path):
        self.genome2dict(input_path,filename,format)
        self.telo_fragment_extract(Genome, arm, self.mstr, start, end, step_size)
        self.file_write(self.dict, output_path)

# C elegans
def main():
    for i in ('L','R'):
        print(i)
        telo = Telo_fragment('ttaggc')
        telo.run("/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/"\
            "genomes/Caenorhabditis Genomes/elegans/",
                'CB4856.fna',
                'fasta',
                'CB4856',
                 i,
                 0,
                 100000,
                 5000,
                 "/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/genomes/"\
                 "Caenorhabditis Genomes/elegans/blastable index/")


main()







#######################################################################################################################
lst = ("GCA_016989505.1_DL238_Canu_genomic.fna",
    "GCA_013403715.1_ASM1340371v1_genomic.fna",
    "GCA_016989095.1_QX1794_Canu_genomic.fna",
    "GCA_016989105.1_MY2693_Canu_genomic.fna",
    "GCA_016989115.1_NIC526_Canu_genomic.fna",
    "GCA_016989125.1_XZ1516_Canu_genomic.fna",
    "GCA_016989145.1_NIC2_Canu_genomic.fna",
    "GCA_016989235.1_MY2147_Canu_genomic.fna",
    "GCA_016989245.1_JU2600_Canu_genomic.fna",
    "GCA_016989275.1_JU310_Canu_genomic.fna",
    "GCA_016989285.1_JU2526_Canu_genomic.fna",
    "GCA_016989295.1_EG4725_Canu_genomic.fna",
    "GCA_016989365.1_JU1400_Canu_genomic.fna",
    "GCA_016989385.1_ECA396_Canu_genomic.fna",
    "GCA_016989455.1_ECA36_Canu_genomic.fna")

pthL = '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/elegans igv/telo_fastas/L/'
pthR = '/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/elegans igv/telo_fastas/R/'


for i in lst:
    os.mkdir((f'{pthL}{i}/'))
    os.mkdir((f'{pthR}{i}/'))


for j in lst:
    for i in ('L','R'):
        print(i)
        telo = Telo_fragment('ttaggc')
        telo.run('/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/'\
            'genomes/Caenorhabditis Genomes/elegans/',
                j,
                'fasta',
                j,
                i,
                0,
                100000,
                5000,
                f'/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/'\
                f'igv_sessions/elegans igv/telo_fastas/{i}/{j}/')
