"""
cd into this directory
run using: python 1_for_loop.py
"""

print("Example 1:")
# All python loops are For Each loops that you might have seen in Java
# You loop through iterables, so if you read documentation that a data
# structure is an iterable then you can loop through it

# for x in range(n) goes from 0 to n-1
for x in range(10):
    print(x)

print("Example 2:")

# for x in string goes through the characters of the string
for x in "banana":
    print(x)

print("Example 3:")

# for x in range(a, b) goes from a to b-1
for x in range(2, 6):
    print(x)

print("Example 4:")

# for x in range(a, b, c) goes from a to b-1, incrementing by c
for x in range(2, 30, 3):
    print(x)

# Useful looping functions

print("Example 5:")

# Enumerate adds an index to whatever you are looping through
for index, value in enumerate('banana'):
    print(f"{index}: {value}")

""" This is equivalent to:
    index = 0
    for value in 'banana':
        print(f"{index}: {value}")
        index+=1
        """

print("Example 5:")

# Zip allows you to iterate through 2 iterable simultaneously
for v1, v2 in zip('bananas', "yummers"):
    print(f"{v1} : {v2}")
