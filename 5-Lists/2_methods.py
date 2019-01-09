"""
cd into this directory
run using: python 2_methods.py
"""

empty_list = []

non_empty_list = [1,4,5,234,675,234]

"""
Useful methods on lists:

len(list)
append(x)
insert(i,x)
list.remove(x)
del list[indices]

More can be found at: https://docs.python.org/3/tutorial/datastructures.html
"""

# indexing into a list
first_element = non_empty_list[0]
second_element = non_empty_list[1]
last_element = non_empty_list[-1]
last_element = non_empty_list[len(non_empty_list) - 1]

first_3_elements = non_empty_list[0:3]

print(first_3_elements)

# examples of methods on lists

empty_list.append(100)
empty_list.append(200)
empty_list.insert(0,50)
print(empty_list)

empty_list.remove(100)
del empty_list[0:2]
print(empty_list)
