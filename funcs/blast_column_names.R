#!/usr/bin/env Rscript
# Libraries
suppressWarnings(suppressMessages(library(dplyr)))
suppressWarnings(suppressMessages(library(optparse)))

option_list = list(
        make_option(c("-f", "--file"), type="character", default=NULL,
                    help="output blastn.txt file", metavar="character")
);
opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);



if (is.null(opt$file)){
        print_help(opt_parser)
        stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

opt_parser = OptionParser(option_list=option_list);
opt = parse_args(opt_parser);



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

file = opt$file
tbl <- read.table(file)
colnames(tbl) <- new_cols
write.table(tbl,file)




