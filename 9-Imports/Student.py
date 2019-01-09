"""
CLASS DEFINITION
"""
class Student:
  # arguments needed to invoke an instance of the object
	def __init__(self, name, student_id):
  	# instance variables
		self.name = name
		self.student_id = student_id

	def getName(self):
		return self.name
