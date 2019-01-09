"""
cd into this directory
run using: python 1_strings.py
"""

print("Printing string literal!")

first_name = "Gideon"
last_name = "Pfeffer"

print(first_name)
print(last_name)

# string can use single or double quotes
print('oooh' == "oooh")

# this is useful to avoid lots of escape characters in strings that use quotes
no_escapes = 'Even though I said "You don\'t need to escape quotes since you can use either" there are times ' \
             'it is unavoidable'

# can use triple quotes of either single or double quotes for string literals
block_quote = """You basically don't have to use escape characters in triple quotes strings
                \n unless you want to then\t"go for it" but you don't have to escape quotes and everything
                is literal."""

# concatenating
full_name = first_name + " " + last_name

print("Full name: " + full_name)

# formatting strings new in versions of python 3.6
fancy_string_variable = f"we can plug variables into strings like {first_name}!"
fancy_string_expression = f"Or we can evaluate expressions in strings the same way {3*2+5} {first_name+' '+last_name}"

print(fancy_string_variable)
print(fancy_string_expression)

# old ways to format not worse but different uses
formatting_v2 = "you can insert variables into strings with: {1} {0}".format(last_name, first_name)

print(formatting_v2)

# an even older version
formatting_v3 = "%s %s" % (first_name, last_name)

print(formatting_v3)

# Like C strings are character arrays in python! no special .getCharAt() functions
first_letter_full_name = full_name[0]

# However strings are immutable so you cannot do assignment
# full_name[0] = '$'

# Strings are iterables which means you can do all the iterable things you will learn later with them as well
