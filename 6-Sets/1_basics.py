"""
cd into this directory
run using: python 1_basics.py
"""

"""
Sets can be though of as unordered lists that cannot contain duplicates
For this reason, you cannot index using [], and you cannot have duplicates in a set
"""

empty_set = set()

non_empty_set = {1,2,3}


print("Empty Set: " + str(empty_set))
print("Nonempty Set: " + str(non_empty_set))
if not empty_set:
	print(f"Empty sets evaluate to None in booleans")

# iterating through the elements
for element in non_empty_set:
	print(element)

# Can quickly check whether or not an element exists in the set [O(1) for sets, O(n) for lists]
if 3 in non_empty_set:
	print("non-empty-set contains 3")

# can add, remove, and clear
non_empty_set.add(10)
non_empty_set.remove(3)

print("Nonempty Set: " + str(non_empty_set))

non_empty_set2 = {1, 10, 6}

# can also or, and and sets together

# Or'ing results in all elements contained by either of them
print("Oring " + str(non_empty_set2 | non_empty_set))

# And'ing results in all elements contained by both of them
print("Anding: " + str(non_empty_set2 & non_empty_set))

"""
More advanced use cases can be found at:
https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
"""