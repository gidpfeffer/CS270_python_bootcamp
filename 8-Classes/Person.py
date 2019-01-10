"""
cd into this directory
run using: python Person.py
"""

"""
CLASS DEFINITION
"""
class Person(object):
	# class variables
	planet_living = 'Earth'

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

# Basic info on using classes. Every function should have a parameter called self, and it should realistically always
# be the very first parameter. This is how you reference the object the function is being called on. This is the
# equivalent of the "" this "" keyword in java.

# Naming functions or variables by prefixing a single or double underscore actually does something.
# These are the roughly equivalent protected and private keywords from java. You will not
# have to use this feature, but you might see it in code we give you.

# There is multiple inheritance, but it is outside the scope of the bootcamp


# Words of caution!!!
# You can assign attributes to objects unintentionally that will
# only be accessible by that particular instance of the class

# Note that if the class does not inherent from a parent class no parans are needed
class foo:
	def __init__(self):
		self.x = 5

z = foo()
z.y = 10
print(z.x, z.y)
z2 = foo()
# The following line will throw an error since z2 does not have an attribute y ONLY z does
# print(z2.x, z2.y)
