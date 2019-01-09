"""
cd into this directory
run using: python Person.py
"""

"""
CLASS DEFINITION
"""
class Person:
  # arguments needed to invoke an instance of the object
	def __init__(self, name, age):
  	# instance variables
		self.name = name
		self.age = age

	def growUp(self):
		self.age = self.age + 1

	def setName(self, newName):
		self.name = newName

	def getAge(self):
		return self.age

	def getName(self):
		return self.name


"""
CODE WHICH WE ARE RUNNING
"""

# Creating an instance of the class, also know as an object
person1 = Person("Gideon Pfeffer", 21)

# Creating a second object
person2 = Person("Guido van Rossum", 62)

# the age is associated with the instance, or object
print(person1.getName() + " is " + str(person1.getAge()) + " years old")
# invoking methods changes this
person1.growUp()
print("After aging " + person1.getName() + " is now " + str(person1.getAge()) + " years old")

# different than person 1, because it is a different object with different instance variables
print(person2.getName() + " is " + str(person2.getAge()) + " years old")

# you can also directly access instance variables, though this is generally bad practice
print(person2.name + " is " + str(person2.age) + " years old")