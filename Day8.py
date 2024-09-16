# String formating in python

'''
letter = "Hey i am from {} and I am from {}"
country = "India"
name = "Shubham"

#print(letter.format(name,country))

print(f"Hey my name is {name} and I am from {country}")
'''

'''
txt = "for only{price:.2f} dollars"
print(txt.format(price=49.01009))
'''

'''
price =49.02304
txt = f"For only {price: .2f} dollars!"
print(txt)
'''

# Docstrings
'''
    Python docstring are the string literals that appear right after the defination of a function, method , class or module.
'''

def square(n):
    ''' Takes the number n, return the square of n'''
    print(n**2)
square(5)
print(square.__doc__)     # print the comment


# Comments vs Docstrings
'''
Comments are discriptions that help programmers better understand the intent and functionality of the program.
    they are completely ignored by the python interpreter.

Docstrings are strings used right after the defination of a function,method, class or module.
    they are used to document our code.
    we can aceess these docstrings usinf=g the doc attribute.
'''


# PEP8
'''
    Document tht provide guidelines and best practices on how to write python code.
    PEP stands for Python Enhancement propsal
'''

# The Zen of python