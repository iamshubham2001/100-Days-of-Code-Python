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
print(square.__doc__)