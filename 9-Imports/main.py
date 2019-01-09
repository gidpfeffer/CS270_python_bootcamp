"""
cd into this directory
run using: python main.py
"""

# IMPORTAING CLASSES FROM OTHER FILES
from Course import Course
from Student import Student

ai_course = Course("Conitzer", "CS 270")
student1 = Student("Gideon", 1)
student2 = Student("John", 2)

ai_course.addStudent(student1)
ai_course.addStudent(student2)

students = ai_course.getStudents()
names = [students[id_num].getName() for id_num in students.keys()]

print(ai_course.getName() + " has " + str(len(students)) + " students and they are named " + str(names))

# Importing python standard libraries, for example the math library can be done as follows
import math
# more information can be found at https://docs.python.org/3/library/math.html

# take logarithms with math library
print(math.log2(1024))

# take cosines, sines, inverse trig, etc also with math library
print(math.cos(math.pi))
