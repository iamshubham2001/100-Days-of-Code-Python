# print("shubham")


# Match case statement ---> Switch Statement


'''
x = int(input("Enter your Number: "))
match x:
    case 0:
        print("x is zer0")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

'''

# The Match case consists of three main entities
#  1. The match keyword
#  2. One or more case clause
#  3. Expression for each case


# For Loop  ---> iterating over a sequence is nothing but iterating over string.

# --> to execute a group of statements a certain number of time
#  for loop     while loop


'''
name=input()
for i in name:
    print(i)
    if(i=='b'):
        print ("This is something special")
'''

'''
colors =["red", "Green", "Blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)
'''

# range
#   --> start
#   --> stop
#   --> step

'''
for k in range(5):
    print(k)
'''
'''
for k in range(1,9):
    print(k)
'''
'''
for k in range(1,12,2):
    print(k)
'''

'''
# Multiplication table of 8 using a loop

# Define the number for which the multiplication table is needed
num = 8

# Loop through numbers 1 to 10
for i in range(1, 11):
    # Print the result of multiplying 8 by i
    print(num * i)

'''

# while loop
'''
i = int(input("Enter the number: "))
while(i<38):
    print(i)
    i = i+1
print("Done with the loop")
'''

'''
i = int(input("Enter the number: "))
while(i<38):
    i = int(input("Enter the number: "))
    print(i)
print("Done with the loop")
'''


#Decrementing while loop

count =5
while(count>0):
    print (count)
    count=count-1
else:
    print("i'm inside else")