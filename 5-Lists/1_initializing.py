"""
cd into this directory
run using: python 1_initializing.py
"""

empty_list = []

non_empty_list = [1,4,5,234,675,234]

# Quick note on Tuples they are the exactly like lists except that they are immutable
# and list functions don't work on them

print("Empty List: " + str(empty_list))
print("Nonempty List: " + str(non_empty_list))
if not empty_list:
	print(f"Empty Lists evaluate to None in booleans")

# iterating through the elements
for element in non_empty_list:
	print(element)

# adding one to all elements in the list lots of ways to do
# Java way
for i in range(len(non_empty_list)):
	non_empty_list[i] = non_empty_list[i] + 1
print("Nonempty List: " + str(non_empty_list))

# Pythonic way
for index, value in enumerate(non_empty_list):
	non_empty_list[index] = value+1
print("Nonempty List: " + str(non_empty_list))

# Note that the next two options do not change the original list and instead make new ones
# doing again in one line using list comprehension (advanced and never needed, just shorter)
non_empty_list = [element + 1 for element in non_empty_list]
print("Nonempty List: " + str(non_empty_list))

# more superfluous using map
map(lambda x: x+1, non_empty_list)
print("Nonempty List: " + str(non_empty_list))

# More on list comprehensions
# List comprehensions are powerful but you can always do without
first_ten_squares = [x**2 for x in range(10)]
print(first_ten_squares)

# you can use multiplication on lists
ten_zeroes = [0]*10
print(ten_zeroes)

# This uses the same object for every entry though which might have unintended consequences
# use list comprehensions instead

ten_lists = [[]]*10
print(ten_lists)

ten_lists[0].append(1)
print(ten_lists)

better_ten_lists = [[] for _ in range(10)]
print(better_ten_lists)

better_ten_lists[0].append(1)
print(better_ten_lists)
