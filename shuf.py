#!/usr/bin/python
import sys
import argparse
import random 
import string 
def parse_input_range(input_range):
    try:
        start, end = map(int, input_range.split('-'))
        return list(range(start, end + 1))
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid input range.")

parser = argparse.ArgumentParser() #argumentParser 
parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help = 'With no FILE, or when FILE is -, read standard input.') # read in file, if none, defaults to stdin 
parser.add_argument('-n','--head-count',type = int,help ='output at most COUNT lines',metavar = "COUNT")  #-n flag and --head-counts flag
parser.add_argument('-i','--input-range',type=parse_input_range,help  ='treat each number LO through HI as an input line',metavar = 'LO-HI')  #-o flag and --output-file flag
args = parser.parse_args()   #saves the arguments in a dictionary that correspond to each inputflag

if args.input_range:              #defines strings to read based on the input range from -i
      lines = [f'Line {number}\n' for number in args.input_range]
else:
    # Read lines from input file or stdin makes sure to add new line
    lines = [line.rstrip('\n') + '\n' for line in args.file.readlines()]      

if args.repeat:
    selected_lines = random.choices(lines, k=args.head_count)
else:
    # Shuffle lines and select unique lines if -r flag is not provided (n flag)
    random.shuffle(lines)
    selected_lines = lines[:args.head_count]

sys.stdout.writelines(selected_lines)