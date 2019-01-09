"""
cd into this directory
run using: python 1_initializing.py
"""

empty_list = []

non_empty_list = [1,4,5,234,675,234]

print("Empty List: " + str(empty_list))
print("Nonempty List: " + str(non_empty_list))

# iterating through the elements
for element in non_empty_list:
	print(element)

# adding one to all elements in the list
for i in range(len(non_empty_list)):
	non_empty_list[i] = non_empty_list[i] + 1

print("Nonempty List: " + str(non_empty_list))	

# doing again in one line using list comprehension (advanced and never needed, just shorter)
non_empty_list = [element + 1 for element in non_empty_list]

print("Nonempty List: " + str(non_empty_list))	