# Telomere Homology Imperfection Elucidation Function (THIEF)

---


## Usage

```
cd desired/directory/ # where THIEF will be cloned to
git clone github/MikeLippincott/THIEF # clone THIEF
cd ../ # step back 
python THIEF # initialize  Thief structure
cd THIEF 
./run_thief.sh -t ttaggg     # run thief with arg "-t ttaggg" ttaggc is telomere sequence input
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
$ 4.1.1
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
```
'