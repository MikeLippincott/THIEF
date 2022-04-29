import os

# Set up sub directories
def set_up_dirs(PATH):
    import os
    if not PATH.endswith('/'):
        PATH = PATH + '/'
    # List of relative PATH's to create if not present
    lst = ['Input_Files/',
           'Input_Files/Genome/',
           'Input_Files/gnbk/',
           'Input_Files/fasta/',
           'Output_files/',
           'Output_files/csv/',
           'Output_files/blast_results/']
    for i in lst:
        ifExist = os.path.exists(f'{PATH}{i}')
        if not ifExist:
            os.makedirs(PATH)


def main():
    return

if __name__ == '__main__':
    main()



#
# parent_dir
#     -Input_files
#         -Genomes
#             -Genome1
#         -Gnbnk
#         -Fastas
#             -Genome1
#                 -L
#                 -R
#             -Genome2
#                 -L
#                 -R
#     -Ouput
#         -csv
#             -Genome1
#                 ...output.csv
#                 ...filtered.csv
#                 ...blast.csv
#                 ...blast.fasta
#         -blast_results
#             -Genome1
#                 -db_Genome1
#                 ...blastn.txt
#                 ...blastn.txt.bed