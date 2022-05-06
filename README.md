# Telomere Homology Imperfection Elucidation Function (THIEF)

---


## Usage

### Clone Repository
```
cd desired/directory/ # where THIEF will be cloned to
git clone github/MikeLippincott/THIEF # clone THIEF
```
#### Main THIEF Module

```
cd THIEF/location/ 
# run thief with arg "-s ttaggg" ttaggg is mammalian telomere sequence input
bash run_thief.sh -s ttaggg     
```
#### Non-Complete Genome Assembly Telomere Scanning (N-GATS) 
```
cd THIEF/location/ 
# -g genome name complete reference assembly
# -i genome name contig level assembly
bash Misc_funcs/Contig_blast.sh -g genome1 -i genome2
```
The Author recommends running in a venv
## Dependencies
##### Python
```
python 3.9
argparse
subprocess
time
os
Bio
pandas
numpy
```
##### R
```
4.1.1
dplyr
optparse
stringr
```
##### Bash
```
BLAST+
```
BLAST + can be obtained [here](https://www.ncbi.nlm.nih.gov/books/NBK569861/)

### THIEF File Structure
```
|-- parent_dir
    |-- funcs
    |-- Input_files
        |-- Genomes 
        |-- Fastas    
            |-- L
                |-- Genome1    
            |-- R
                |-- Genome1     
    |-- Ouput  
        |--csv 
            |-- Genome1   
                |-- ...output.csv  
                |-- ...filtered.csv  
                |-- ...blast.csv  
                |-- ...blast.fasta  
        |-- blast_results  
            |-- Genome1  
                |-- db_Genome1  
                |-- ...blastn.txt  
                |-- ...blast2bed.txt
                |-- ...blast2bed.txt.bed  
    |-- Misc_funcs
        |-- Output
            |-- Blast
                |-- Genome2
                    |-- db_Genome2
                    |-- ...blastn.txt
            |-- Index
                |-- Genome1
                    |-- ...Indexfile.txt
            
```
