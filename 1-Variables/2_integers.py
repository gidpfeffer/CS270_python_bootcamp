"""
cd into this directory
run using: python 2_integers.py
"""

lucky_number = 3234
print("My lucky number is:")
print(lucky_number)

# concatenating, must be a string, use str()
print("My lucky number concatenated is: " + str(lucky_number))

# No ++ operator to increment by one but other cool ways to do it
index = 0
index += 1
# This is the same as : index = index+1
# This works with all the operators so you can do +=, *=, -=, /=, %= to the same effect

# there are two ways to exponentiate
power = 3
expo_1 = lucky_number**power
expo_2 = pow(lucky_number, power)

print(expo_1, expo_2)

# When exponetiating large numbers or with large powers use the second option it is much faster, and has a mod option
print(pow(2, 1000000, 5))

# the modulus operator is %
print(31 % 3)

# be careful with stupid large numbers as ints are not bound by 32 or 64 bits and will take up as much space as needed
# will compile but will take forever and probably cause a system memory error: pow(2, 1000000000000000)

# random might be useful knowledge not needed for course
# numbers can have an underscore in them that will not appear in the result
small_prime = 26_9

print(small_prime)

# complex numbers are cool as well just use j
complex_num = 1+2j

print(f'{complex_num} squared is: {complex_num**2}')


