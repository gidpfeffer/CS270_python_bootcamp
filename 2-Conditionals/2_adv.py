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

# is checks for object equality where == does value equality
# don't use the keyword is for integers or floats
# ex

if 10000 is 10000:
	print("10000 is 10000")

if 10000 is pow(10, 4):
	pass
else:
	print("10000 is NOT pow(10, 4)")

# If you want to see some crazy magic that results from this ask Colter

# not negates the statements
#ex
if not False:
	print("Not False is True")

# So we can write
if not a < 10 and not a > 10:
	print("a is 10")

# There is no Null but we do have None and None is false
if not None:
	print("None is false")

# there is a ternary operator it is contentious use at own risk
