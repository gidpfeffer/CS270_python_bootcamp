"""
CLASS DEFINITION
"""
class Course:
  # arguments needed to invoke an instance of the object
	def __init__(self, teacher, course_name):
  	# instance variables
		self.teacher = teacher
		self.course_name = course_name
		self.students = dict()

	def addStudent(self, new_student):
		self.students[new_student.student_id] = new_student

	def removeStudent(self, removing_student):
		self.students.pop(removing_student.student_id, None)

	def getStudents(self):
		return self.students

	def getName(self):
		return self.course_name
