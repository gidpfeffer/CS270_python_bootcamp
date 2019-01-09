"""
cd into this directory
run using: python 2_cat.py filepath

cat is a standard Unix program which prints out the contents of a file line by line. 
Below is a simple python implementation.

Examples Uses:
python 2_cat.py data/data1.txt
python 2_cat.py data/data2.txt
python 2_cat.py 2_cat.py
"""

# Uses the python standard library package sys
import sys

if len(sys.argv) != 2:
	print(f'Invalid Arguments: usage is `python 2_cat.py [filepath]`')
	exit(1)

filepath = sys.argv[1]

with open(filepath) as f:
    for line in f:
        print(line)