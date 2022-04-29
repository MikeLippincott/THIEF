library(dplyr)

# add column names onto blast results (tabular)

new_cols <- c('query',
              'genome',
              '%Match',
              'length',
              '#.of.Mismatches',
              '#.of.Gaps',
              'Alignment_Start_in_q',
              'Alignment_End_in_q',
              'Alignment_Start_in_ref',
              'Alignment_End_in_ref',
              'evalue',
              'bitscore',
              'query seq aligned',
              'ref seq aligned')

setwd("/Users/mike/OneDrive - Maryville University/Ahmed Stuff/IGV_Telomeres/Blast Results/")
list.files(getwd())
lst <- c("ALT1_blastn.txt",   
        "ALT2_blastn.txt",      
        "ALT3_N2_blastn.txt",   
        "ALT3_WS274_blastn.txt",
        "ALT4_N2_blastn.txt",   
        "ALT4_WS274_blastn.txt",
        "CB4856_blastn.txt",    
        "Human_blastn.txt",     
        "Tyson_N2_blastn.txt",  
        "Tyson_WS274.txt",      
        "WB235_blastn.txt",     
        "WS274_blastn.txt")    
for (i in lst){
        tbl <- read.table(i)
        colnames(tbl) <- new_cols
        write.table(tbl,i)
}

tbl <- read.table("WS274_blastn.txt")
head(tbl)
colnames(tbl) <- new_cols
write.table(tbl,"WS274_blastn.txt")




