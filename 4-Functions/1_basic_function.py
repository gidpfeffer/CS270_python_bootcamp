"""
cd into this directory
run using: python 1_basic_function.py
"""

def addAndDivideBy5(a, b):
	return (a + b)/5.0

def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result = result * i
	return result

c = addAndDivideBy5(10, 15)

factorialOfFive = factorial(5)

print("(10 + 15)/5 = " + str(c))

print("5! = " + str(factorialOfFive))