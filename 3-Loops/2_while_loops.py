"""
cd into this directory
run using: python 2_while_loops.py
"""

print("Example 1:")

# while (expr) keeps going until expression evaulates to false
i = 0
while i < 5:
	print(i)
	i = i + 1

print("Example 2:")

# will never enter loop because evaluates to false
while False:
	print("This Should Not Print!")

print("Example 3:")

# 
i = 0
while i is not 20:
	print(i)
	i = i + 5

print("Example 4:")

print("What is i now? " + str(i))
