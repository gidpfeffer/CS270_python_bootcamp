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