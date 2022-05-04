
# args
while getopts g:f: flag
do
  case "${flag}" in
    t) teloseq=${OPTARG};;
  esac
done


# loop through all files in dir
for file in Input_files/Genomes/*; do
  genome="$(basename "$file")" # basename with extension
  genome_name="$(basename "$file" .fna)" # basename with no extension
  pl="Input_Files/Fasta/L/${genome_name}/" # L dir
  pr="Input_Files/Fasta/R/${genome_name}/" # R dir
done

echo ${genome}
echo ${genome_name}
echo ${pl}
echo ${pr}


python funcs/main.py -pl ${pl} -pr ${pr} -t ${teloseq} -g ${genome}

