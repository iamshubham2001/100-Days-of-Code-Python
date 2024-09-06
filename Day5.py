# break and continue
# ---> the break statement enables a program to skip over a part of the code. a break statement terminates the very loop it lies within.

'''
for i in range(12):
    print("5 X", i+1, "=", 5*(i+1))
    if(i==10):
        break

#print("Loop ko chodker nikal gaya")
'''

'''
for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X", i+1, "=", 5* i)
    if(i==10):
        break
'''

'''
for i in [2,3,4,5,6,8,0]:
    if(i%2!=0):
        continue
    print(i)
'''


# Do-While loop ---> a loop in which a set of instruction  will execute at least once.
'''
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break
'''

# Function

'''
    --> A function is a block of code that performs a specific task whenever it is called.
        In bigger program, whenever we have large amount of code, it is advisable to create or use existing function that make the program flow organized and neat.

        There are two type of functions:
        1. Built-in   
            --> These function are defined and pre coded in python.
                not use def()
                eg -> min(), max(), len(), sum(), type(), list(), tuple(), set(), print(), range()
        2. user-defined
            --> We can create functions to perform specific task as pe rour needs.
                use def()
'''


def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

def isLesser(a,b):
    pass


a=9
b=8
# if(a>b):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a,b)
isGreater(a,b)

c = 4
d = 2
# gmean2 = (c*d)/(c+d)
# print(gmean2)
# if(c>d):
#     print("first number is greater")
# else:
#     print("second number is greater or equal")
calculateGmean(c,d)
isGreater(c,d)

def name(name,lname):
    print("hello, ", name, lname)
name("Shubham","Sharma")
