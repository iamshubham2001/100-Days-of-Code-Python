# Variable && Data types
# variabe is like a container that holds Data
# Data types specific the type of value a variable holds.
# In python we can print the type of any operator using type function:

'''
a=complex(8,2)
print(a)
a1 = 9
b = "harry" 
print(b)
print(a+a1)
d=None
c=True
print("the type of a is", type(a))
print("the type of a is", type(b))
print("the type of a is", type(d))
print("the type of a is", type(c))
'''

# Numeric Data type : int, float, Complex
# Text data : str
# Boolean data : True,False
# Sequenced data : list, tuple
# Mapped data : dict


# Calculator

'''
print(5+6)
print(5-6)
print(5*6)
print(5/6)
print(5//3)     #Floor Division
print(5%6)    #Modulus
print(5**6)  # Exponential

'''

# Typecasting 
#       --> The conversion of one data type into the other data type is known as type casting in python or type conversion in python
#      Types :
#         1. Explicit --> mai ker raha hu
#         2. Implicit --> 

'''
a = "1"
b = "2"
c = "Harry"
d = "Bhaii"
print(a+b)
print(c+d) 
print(int(a)+int(b))   '''

# Implicit Type Casting
'''
c=1.9
d=8

print(c+d) '''

# take user input in python
#  --> we can take user input directly by using input() function
#  --> input function gives a return value as string/character

'''
# a = input()

a = input("Enter your name = ") 
print("my name is ",a)
'''

a = input("enter the number: ")
d = input("enter the number: ")
print(a+d)
print(int(a)+int(d))

b = int(input("enter first number: "))
c = int(input("enter your second number: "))
print(b+c)
