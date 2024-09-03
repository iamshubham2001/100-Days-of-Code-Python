# String method
# Strings are immutable

'''
a = "Harry!! !!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","John"))
print(a.split(" "))

blogheading = "introduction tO js"  #capitalize
print(blogheading.capitalize())

s ="Welcome to the console"
print(s.center(50))
print(len(s))
print(len(s.center(50)))
print(a.count("Harry"))     # Count

'''

# find() method  --> it searches the first occurance of the given value and returns the index where it is present.

'''
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.index("is"))
'''

# index is same as find but it not return -1


# isalnum() --> Method return true only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it return false.

'''
str1= "WelcomeTOTheConsole"
print(str1.isalnum())
'''


# islower()


# isprintable()  --> Return true if all the values within the given string are printable,if not, then return False.
# swapcase()
# title()


# Conditional operator
# <, >, >=, <=, ==, !=

# --> if
# --> if-else
# --> if-else-elif
# --> nested if-else-elif

'''
a = int(input("Enter your age: "))
print("your age is: ", a)

if(a>18):
    print("You can drive")

else:
    print("you can't drive")
'''

#elif
'''
num = int(input())
if(num < 0):
    print("number is negative.")
elif(num==0):
    print("number is zero.")
else:
    print("number is positive.")
'''

# Nested if Statement

num = int(input())
if(num < 0):
    print("number is negative.")
elif(num>0):
    if(num<=10):
        print("no. is b/w 1-10")
    elif(num > 10 and num <= 20):
        print("no. is b/w 10 to 20")
    else:
        print("number is greater than 201.")
else:
    print("number is zero.")
