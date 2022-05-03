import os



# Set up sub directories
def set_up_dirs(dir):
    import os
    PATH = os.getcwd()
    if not PATH.endswith('/'):
        PATH = PATH + '/'
    print(PATH)
    # List of relative PATH's to create if not present
    ifExist = os.path.exists((f'{PATH}{dir}/'))
    print(ifExist)
    if not ifExist:
        os.makedirs((f'{PATH}{dir}/'))


def main():
    return

if __name__ == '__main__':
    main()




parent_dir
    -Input_files
        -Genomes
            -Genome1
        -Gnbnk
        -Fastas
            -Genome1
                -L
                -R
            -Genome2
                -L
                -R
    -Ouput
        -Genome1
            -csv
                ...output.csv
                ...filtered.csv
                ...blast.csv
                ...blast.fasta
            -blast_results
                -db_Genome1
                    ...blastn.txt
                    ...blastn.txt.bed


