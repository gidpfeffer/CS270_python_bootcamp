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

# Using the with keyword means you do not have to worry about closing the file when you are done with it
# the file is closed as soon as the program leaves the scope of the with statement
with open(filepath) as f:
    for line in f:
        print(line, end="")