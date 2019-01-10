"""
cd into this directory
run using: python main.py
"""

# IMPORTING CLASSES FROM OTHER FILES
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


# Other ways to import, and common paradigms
import FooBar

# if we want the bar class
bar = FooBar.Bar()
# Or
import FooBar as FB

# we can now use FB instead of FooBar
bar = FB.Bar()

from FooBar import foo_bar as fb_generator

foo, bar = fb_generator()

# Worst practise but you will see it is to use the * operator to import everything
from FooBar import *
foo_bar()

# Word of caution!!

# beware of circular imports! Two file can't both import each other
# That is Student can't import course while course imports student.
# It will unintuitively throw a import not found error. Be careful with
# excessively importing things.
