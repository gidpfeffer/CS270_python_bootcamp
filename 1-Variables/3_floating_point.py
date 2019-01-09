"""
cd into this directory
run using: python 3_floating_point.py
"""

lucky_number = 24.3421
print("My lucky number is:")
print(lucky_number)

# concatinating, must be a string, use str()
print("My lucky number concatinated is: " + str(lucky_number))

# integer math gets rounded down
print(12/5)

# decimals indicate the result should be floating point
print(12.0/5)

"""
In python 3, both of the above statements will resolve to floating point, in python 2.7, only the bottom one will
"""

# Math symbols are +, -, /, and *, for adding, subtracting,  dividing, and multiplying respectively
# Parentesis maintain order of operations

# ex
print((12.0/5 + 2 - 9.1)/3.0)