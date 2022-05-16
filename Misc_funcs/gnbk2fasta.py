import os

# Ape file (Genbank) -> fasta
# Throwing a parsing error, decided to parse myself...
# from Bio import SeqIO
# SeqIO.read("file.ape","genbank")


def gnbk2fasta(path_n_gnbkfile): #file and path
    # Extract filename
    filename = os.path.basename(path_n_gnbkfile)
    path = os.path.dirname(path_n_gnbkfile)
    basename = filename.replace('.csv','')
    # Extract Genbank sequence
    file = open(path_n_gnbkfile,'r')
    data = file.read()
    lst = data.replace('\n','').split('ORIGIN')[1]
    lst = lst.replace(' ','')
    lst = ''.join(i for i in lst if not i.isdigit())
    seq = lst.replace('//','')
    file.close()
    # Write to fasta file
    outfilename = f'{path}/{basename}.fasta'
    outfile = open(f'{path}/{basename}.fasta','w')
    outfile.write((f'>{basename}\n'))
    outfile.write(seq)
    outfile.close()


def call (path):
    paths = [f.path for f in os.scandir(path) if f.is_file()]
    for i in paths:
        if i.endswith('.ape'):
            print(i)
            gnbk2fasta(i)

call('/Volumes/MLIPPINCOTT/Genomics/genomes/human genome/FASTA/GCA_021950905.1_HG002.pat.cur.20211005_genomic')
call('/Volumes/MLIPPINCOTT/Genomics/genomes/human genome/FASTA/GCA_021951015.1_HG002.mat.cur.20211005_genomic')


