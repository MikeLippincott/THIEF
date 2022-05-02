#!/usr/bin/env Rscript

library(optparse)

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



f <- function(s1, s2) {
    print(s1)
    print(s2)
}
f(opt$file, opt$organism)
print('works')