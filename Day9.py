#------------------Recursion--------------

'''Recursion is the process of defining something in terms of itself'''
# factorial(7)=7*6*5*4*3*2*1
# factorial(6)=6*5*4*3*2*1
# factorial(5)=5*4*3*2*1
# factorial(4)=4*3*2*1
# factorial(3)=3*2*1
# factorial(0)=1

# factorial(n) = n * Factorial(n-1)

'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
# print(factorial(4))
# print(factorial(5))
n=int(input("Enter the number: "))
print(factorial(n))
'''

# Quick quiz
# Calculation of fibonacci series

'''
f0 = 0
f1 = 1
f2 = f1 + f0
fn = fn-1 + fn-2
'''

'''
def fabonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fabonacci(n-1)+fabonacci(n-2))
    
n = int(input("Enter the number: "))
print(fabonacci(n))

'''

#--------Set-----------
''' Set is a collection of well defined object
    do not contain duplicate item
    Sets are unchangeable
    Sets are unordered collection of data item
    { } use curly bracket
'''

s ={2,4,2,6,"carlo","shubham",8}
print(s)


#empty set
harry =set()
print(type(harry))

for value in s:
    print(value)

