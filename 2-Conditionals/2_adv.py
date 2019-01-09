"""
cd into this directory
run using: python 2_adv.py
"""

a = 10

if a < 10:
	print("a is less than 10")
elif a > 10:
	print("a is greater than 10")
else:
	print("a is 10")

# also could do

if a == 10:
	print("a is 10")

# or

if a is 10:
	print("a is 10")

# not negates the statements

#ex
if not False:
	print("Not False is True")

# So we can write
if not a < 10 and not a > 10:
	print("a is 10")

