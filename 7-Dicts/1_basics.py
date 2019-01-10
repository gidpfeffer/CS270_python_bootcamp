"""
cd into this directory
run using: python 1_basics.py
"""

empty_dict = dict()

non_empty_dict = {1: 'a', 2: 'b', 3: 'z'}


print(f'Empty Set: {empty_dict}')
print(f'Nonempty Set: {non_empty_dict}')
if not empty_dict:
	print(f"Empty dicts evaluate to None in booleans")

# iterating through the elements
for key in non_empty_dict:
	print(key)

# can get a value by indexing the dictionary using the key
for key in non_empty_dict:
	print(f'Key: {key}, value: {non_empty_dict[key]}')

# more succinct way
for key, value in non_empty_dict.items():
	print(f'Key: {key}, value: {value}')

# can replace a key with a new value
non_empty_dict[1] = 'd'
print(f'Nonempty Set: {non_empty_dict}')

# can add a new key value pair, and it can be anything, set, list, number, string, another dict, etc
non_empty_dict[6] = ['hello', 'world']
print(f'Nonempty Set: {non_empty_dict}')

# removing a key if it exists
non_empty_dict.pop(1, None)
print(f'Nonempty Set: {non_empty_dict}')

# no error is thrown if it doesnt exist
non_empty_dict.pop(1, None)
print(f'Nonempty Set: {non_empty_dict}')

# can also check for existence of key like in a set
if 1 in non_empty_dict:
	print('1 key exists')
elif 6 in non_empty_dict:
	print('6 key exists')

# useful advanced constructs found at https://docs.python.org/3/library/collections.html

# the one I use the most is a default dict
# in java you probably wrote code that looked like this when working with maps

dict = {}
for i in "bananananana":
	if i not in dict:
		dict[i] = 0
	dict[i] += 1
print("\t".join([f"{k}: {v}" for k, v in dict.items()]))
# we can do this more succinctly using default dicts
# since if an entry is not in the dictionary we always want its
# value to default to the integer 0. These won't throw key errors.
print()
from collections import defaultdict
d = defaultdict(int)
for i in "bananananana":
	d[i] += 1
print("\t".join([f"{k}: {v}" for k, v in d.items()]))
print()
# if you look in the link to the collections page you can see we can
# do this even more succinctly using a Counter object
from collections import Counter
c = Counter("bananananana")
print("\t".join([f"{k}: {v}" for k, v in c.items()]))
