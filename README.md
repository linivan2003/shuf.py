# shuf.py
This Python script pyshuf.py replicates the functionality of the shuf command in Bash. It allows users to shuffle lines or generate random permutations from input files or specified lists.

## Features
Shuffle lines in a file or input list.
Generate random permutations of numbers within a range.
Specify the number of lines or random numbers to output.
Easily customizable through command-line arguments.

## Usage
```bash

# returns shuf foo.txt
python py.shuf foo.txt 

# returns shuf -n 5 foo.txt
python py.shuf -n 5 < foo.txt

# returns shuf -n 5 -i 5 foo.txt
python3 shuf.py -n 5 -i 1-5 < test1.txt
```
