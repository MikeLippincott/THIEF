import os
import shutil
import pandas as pd

# Csv from THIEF -> fasta

def thief_csv2fasta(path_n_csv): #file and path
    # Extract filename
    filename = os.path.basename(path_n_csv)
    path = os.path.dirname(path_n_csv)
    basename = filename.split('.')[0]

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


path = "/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/" \
        "elegans igv/telo_fastas/THIEF_output/" \
       "2022_04_28__11_36_CB4856_Thief_C-elegans_output_table_for_blast.csv"


path = "/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/" \
        "elegans igv/telo_fastas/THIEF_output/" \
       "2022_04_28__11_39_WB235_Thief_C-elegans_output_table_for_blast.csv"
thief_csv2fasta(path)

path = "/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/" \
        "elegans igv/telo_fastas/THIEF_output/" \
       "2022_04_28__11_39_WS274_Thief_C-elegans_output_table_for_blast.csv"
thief_csv2fasta(path)

path = "/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/igv_sessions/Human/THIEF_output/" \
       "2022_04_28__11_43_Thief_Human_output_table_for_blast.csv"
thief_csv2fasta(path)

