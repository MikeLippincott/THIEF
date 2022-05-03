#!/bin/bash

python main.py -pl -pr -of -t -e




parser.add_argument('-pl', '--Lpath',  help="Path containing L arm fastas", type=str)
parser.add_argument('-pr', '--Rpath', help="Path containing R arm fastas",type=str)
parser.add_argument('-of', '--out_file', help="name of output file (no extension)",type=str)
parser.add_argument('-t', '--telo_seq', help="telomere sequence e.g. 'ttaggg' ",type=str)
parser.add_argument('-g', '--genome', help="Genome File for BLAST analysis", type=str)