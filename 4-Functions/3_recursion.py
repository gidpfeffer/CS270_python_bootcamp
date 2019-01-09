"""
cd into this directory
run using: python 3_recursion.py
"""

# a base case returns a fixed value
# a recurrence computed f(n) using f(i) where i is derived from n

def factorial(n):
	# base case
	if n <= 1:
		return 1
	# recurrence
	return n * factorial(n - 1)

print("5! is " + str(factorial(5)))