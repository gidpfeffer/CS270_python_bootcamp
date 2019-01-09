"""
cd into this directory
run using: python 1_basic.py [arguments] 

Examples:
python 1_basic.py Hello World!
python 1_basic.py Words and Numbers 1000 2324 49
"""

# Uses the python standard library package sys
import sys

print(f'Number of arguments: {len(sys.argv)} arguments.')
print(f'Argument List: {sys.argv}')

"""
KEEP IN MIND

1. THE NAME OF THE PROGRAM IS INCLUDED (for example 1_basic.py)

2. ALL ARGUMENTS ARE READ AS STRINGS, THEY CAN BE CONVERTED TO INTEGERS AND FOATS USING

int_var = int(string_var) or float_var = float(string_var) respectively
"""