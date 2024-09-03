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

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.index("is"))

# index is same as find but it not return -1


# isalnum() --> Method return true only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it return false.

str1= "WelcomeTOTheConsole"
print(str1.isalnum())

# islower()


# isprintable()  --> Return true if all the values within the given string are printable,if not, then return False.
# swapcase
# title
