"""
cd into this directory
run using: python 2_optional_args.py
"""

def printName(firstName, lastName=""):
	print("Hi, " + firstName + lastName)

# uses default lastname
printName("Gideon")

# uses passed in lastname
printName("Gideon", " Pfeffer")


def printNameWithAge(firstName, lastName="", age=25):
	print("Hi, " + firstName + lastName + ", you are " + str(age) + " years old")

# Does not work!!, specify which argument is which if out of order
# printNameWithAge("Bob", 12)

printNameWithAge("Bob", age=12)

# Be careful with defualt parameters especially mutable objects
# ex

def add_to_list(x, list=[]):
	list.append(x)
	return list


l = [x**3 for x in range(-2, 5, 2)]
print(l)
l = add_to_list(5, l)
print(l)

new_list = add_to_list(2)
print(new_list)
another_new_list = add_to_list(17)
print(another_new_list)

# you will see that the default list used for the parameter is the same
# across all function calls, it DOES NOT give you a fresh empty list every call

