# Short hand if else -------------------

'''
a = int(input("a: "))
b = int(input("b: "))
print("A") if a>b else print("=") if a==b else print("b")
'''


# Syntax
'''
if condition:
    result = value_if_true
else:
    result = value_if_false
'''


# Enumerate Function------------------------------

'''
    The enumerate function is a built-in function in python yhat allows you to loop over a sequence (such as list, tuple, or string) and get the index and value of each element in the sequence at the same time.
'''


'''
marks =[12, 56, 32, 98, 12, 45, 1, 4]

# index =0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Harry, awesome")
#     index+=1


for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Harry, awesome")
'''

fruits = ['Apple','Banana','Mango']
for index,fruit in enumerate(fruits, start=1):
    print(index,fruit)