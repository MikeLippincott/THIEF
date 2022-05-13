#!/usr/bin/env Rscript
# Libraries
suppressWarnings(suppressMessages(library(dplyr)))
suppressWarnings(suppressMessages(library(stringr)))
suppressWarnings(suppressMessages(library(optparse)))

option_list = list(
        make_option(c("-f", "--file"), type="character", default=NULL,
                    help="input file name", metavar="character"),
        make_option(c("-r", "--organism"), type="character", default="worms",
                    help="Organism Selection for Telomere Sequence [default= %default]", metavar="character")
);
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);



if (is.null(opt$file)){
        print_help(opt_parser)
        stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);



# Import Thief Output & Parameters
thief_worms <- function(full_file_path,telo_seq){
        csvdir <- (full_file_path)
        filepath <- dirname(csvdir)
        filename_nakey <- sub('\\.csv$', '', basename(csvdir)) # No file Extension
        df <- read.csv(csvdir)
        # list of unique sequences (non telomeric)
        uniqueseq <- unique(df$seq)
        # new column stating arm of telomere
        df1 <- df %>%
                mutate(chrom_arm = case_when(
                        startsWith(chrom, "IL") ~ "IL",
                        startsWith(chrom, "IR") ~ "IR",
                        startsWith(chrom, "IIL") ~ "IIL",
                        startsWith(chrom, "IIR") ~ "IIR",
                        startsWith(chrom, "IIIL") ~ "IIIL",
                        startsWith(chrom, "IIIR") ~ "IIIR",
                        startsWith(chrom, "IVL") ~ "IVL",
                        startsWith(chrom, "IVR") ~ "IVR",
                        startsWith(chrom, "VL") ~ "VL",
                        startsWith(chrom, "VR") ~ "VR",
                        startsWith(chrom, "XL") ~ "XL",
                        startsWith(chrom, "XR") ~ "XR"))

        # df1$chrom_arm <- factor(df1$chrom_arm, labels = c("IL","IR","IIL","IIR","IIIL","IIIR",
        #                                                   "IVL","IVR","VL","VR","XL","XR"))
        uniqueseq <- unique(df1$seq)
        df2 <- filter(df1, chrom == 'cow')
        for (i in 1:length(uniqueseq)){
                # df$ID <- df$seq == uniqueseq[i]
                tmp <- df1 %>%
                        mutate(ID = case_when(
                                uniqueseq[i] == seq ~ i))
                df2 <- rbind(df2,tmp)
                df2 <- na.omit(df2)
                nrow(df2)
        }
        df2_no_telo <- df2[!grepl(telo_seq,df2$Telo),]
        file1 <- paste0(filepath,'/',filename_nakey,"_Filtered.csv")
        write.csv(df2_no_telo,file1)
        tmp <- aggregate(data.frame(count = df2_no_telo$seq), list(value = df2_no_telo$seq), length)
        tmp$seq_len <- str_length(tmp$value)
        tmp$sandwhich_seq_L <- paste0(telo_seq,tmp$value)
        tmp$sandwhich_seq_R <- paste0(tmp$value,telo_seq)
        tmp$sandwhich_seq <- paste0(telo_seq,tmp$value,telo_seq)
        file2 <- paste0(filepath,'/',filename_nakey,"_table_for_blast.csv")
        write.csv(tmp,file2)
        print(file1)
        print(file2)
}
thief_humans <- function(full_file_path,telo_seq){
        csvdir <- (full_file_path)
        filepath <- dirname(csvdir)
        filename_nakey <- sub('\\.csv$', '', basename(csvdir)) # No file Extension
        df <- read.csv(csvdir)
        # list of unique sequences (non telomeric)
        uniqueseq <- unique(df$seq)
        # new column stating arm of telomere
        df1 <- df %>%
                mutate(chrom_arm = case_when(
                        startsWith(chrom, "IL") ~ "IL",
                        startsWith(chrom, "IR") ~ "IR",
                        startsWith(chrom, "IIL") ~ "IIL",
                        startsWith(chrom, "IIR") ~ "IIR",
                        startsWith(chrom, "IIIL") ~ "IIIL",
                        startsWith(chrom, "IIIR") ~ "IIIR",
                        startsWith(chrom, "IVL") ~ "IVL",
                        startsWith(chrom, "IVR") ~ "IVR",
                        startsWith(chrom, "VL") ~ "VL",
                        startsWith(chrom, "VR") ~ "VR",
                        startsWith(chrom, "VIL") ~ "VIL",
                        startsWith(chrom, "VIR") ~ "VIR",
                        startsWith(chrom, "VIIL") ~ "VIIL",
                        startsWith(chrom, "VIIR") ~ "VIIR",
                        startsWith(chrom, "VIIIL") ~ "VIIIL",
                        startsWith(chrom, "VIIIR") ~ "VIIIR",
                        startsWith(chrom, "IXL") ~ "IXL",
                        startsWith(chrom, "IXR") ~ "IXR",
                        startsWith(chrom, "XL") ~ "XL",
                        startsWith(chrom, "XR") ~ "XR",
                        startsWith(chrom, "XIL") ~ "XIL",
                        startsWith(chrom, "XIR") ~ "XIR",
                        startsWith(chrom, "XIIL") ~ "XIIL",
                        startsWith(chrom, "XIIR") ~ "XIIR",
                        startsWith(chrom, "XIIIL") ~ "XIIIL",
                        startsWith(chrom, "XIIIR") ~ "XIIIR",
                        startsWith(chrom, "XIVL") ~ "XIVL",
                        startsWith(chrom, "XIVR") ~ "XIVR",
                        startsWith(chrom, "XVL") ~ "XVL",
                        startsWith(chrom, "XVR") ~ "XVR",
                        startsWith(chrom, "XVIL") ~ "XVIL",
                        startsWith(chrom, "XVIR") ~ "XVIR",
                        startsWith(chrom, "XVIIL") ~ "XVIIL",
                        startsWith(chrom, "XVIIR") ~ "XVIIR",
                        startsWith(chrom, "XVIIIL") ~ "XVIIIL",
                        startsWith(chrom, "XVIIIR") ~ "XVIIIR",
                        startsWith(chrom, "XIXL") ~ "XIXL",
                        startsWith(chrom, "XIXR") ~ "XIXR",
                        startsWith(chrom, "XXL") ~ "XXL",
                        startsWith(chrom, "XXR") ~ "XXR",
                        startsWith(chrom, "XXIL") ~ "XXIL",
                        startsWith(chrom, "XXIR") ~ "XXIR",
                        startsWith(chrom, "XXIIL") ~ "XXIIL",
                        startsWith(chrom, "XXIIR") ~ "XXIIR",
                        startsWith(chrom, "X-ChromL") ~ "X-ChromL",
                        startsWith(chrom, "X-ChromR") ~ "X-ChromR",
                        startsWith(chrom, "Y-ChromL") ~ "Y-ChromL",
                        startsWith(chrom, "Y-ChromR") ~ "Y-ChromR"))
        df1$chrom_arm <- factor(df1$chrom_arm, labels = c("IL","IR","IIL","IIR","IIIL","IIIR","IVL","IVR","VL","VR",
                                                          "VIL","VIR","VIIL","VIIR","VIIIL","VIIIR","IXL","IXR","XL","XR",
                                                          "XIL","XIR","XIIL","XIIR","XIIIL","XIIIR","XIVL","XIVR","XVL","XVR",
                                                          "XVIL","XVIR","XVIIL","XVIIR","XVIIIL","XVIIIR","XIXL","XIXR","XXL","XXR",
                                                          "XXIL","XXIR","XXIIL","XXIIR","X-ChromL","X-ChromR","Y-ChromL","Y-ChromR"))

        uniqueseq <- unique(df1$seq)
        df2 <- filter(df1, chrom == 'cow')
        for (i in 1:length(uniqueseq)){
                # df$ID <- df$seq == uniqueseq[i]
                tmp <- df1 %>%
                        mutate(ID = case_when(
                                uniqueseq[i] == seq ~ i))
                df2 <- rbind(df2,tmp)
                df2 <- na.omit(df2)
                nrow(df2)
        }
        df2_no_telo <- df2[!grepl(telo_seq,df2$Telo),]
        file1 <- paste0(filepath,'/',filename_nakey,"_Filtered.csv")
        write.csv(df2_no_telo,file1)
        tmp <- aggregate(data.frame(count = df2_no_telo$seq), list(value = df2_no_telo$seq), length)
        tmp$seq_len <- str_length(tmp$value)
        tmp$sandwhich_seq_L <- paste0(telo_seq,tmp$value)
        tmp$sandwhich_seq_R <- paste0(tmp$value,telo_seq)
        tmp$sandwhich_seq <- paste0(telo_seq,tmp$value,telo_seq)
        file2 <- paste0(filepath,'/',filename_nakey,"_table_for_blast.csv")
        write.csv(tmp,file2)
        print(file1)
        print(file2)
}
organism_error <- function(){
        error_message <- c("Error: Organism not Found.",
                           'Please enter current available options:',
                           'human',
                           'worms')
        msg <- string.break.line(error_message)
        print(str(msg))

}
thief_clean <- function(full_file_path,organism){
        if (organism == 'human'){
                thief_humans(full_file_path,'ttaggg')
        }else if (organism == 'worms'){
                thief_worms(full_file_path,'ttaggc')
        }else
                organism_error()
}

thief_clean(opt$file,opt$organism)

