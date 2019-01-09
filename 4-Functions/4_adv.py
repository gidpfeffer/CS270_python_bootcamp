"""
cd into this directory
run using: python 4_adv.py
"""

# Functions are what is called a First class object in Python.
# I won't talk about about what that is but I will show some implications

# basic function
def bar(x):
    return x+1

# we can call it as normal and see that the function without the call returns an object
print(bar(1))
print(bar)

# Since functions are objects that means we can pass them as parameters to other functions
def foo(x, func=bar):
    return func(x)


def add_5(x):
    return x+5


print(foo(1))
print(foo(1, func=add_5))

# another thing about functions being objects is that you can re assign them (oftentimes unintentionally)
print(bar(10))
bar = add_5
print(bar(10))

# there are good uses of this though for example changing print to some logging function instead
