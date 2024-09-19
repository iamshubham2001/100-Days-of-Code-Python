#-------Dictionary Method----------

'''
ep1 = {122:45, 123:89, 567:69, 670:69 }
ep2 = {222:67, 566:90}

#ep1.update(ep2)
#ep1.clear
#empt={}
#ep1.pop(122)
#ep1.popitem()    ---> delete last item from dictionary
#del(ep1)

print(ep1)
'''


# for Loop with else in python ---------------------

'''
    Python allows the else keyword to be used with the for and while loops too.
    The else block appear after the body of the loop.
    The statements in the else blockwill be executed after all iteration are completed.
    The pgm exists the loop only after the else block is executed. 
'''

'''
for i in range(6):
    print(i)
    # if i == 0:
    #     break    ----> only use if break are not used
    

else:
    print("Sorry no i")
'''


'''
i =0
while i<7:
    print(i)
    i=i+1
    if i ==4:
        break

else:
    print ("Sorry")
'''

'''
for x in range(5):
    print("iteration no. {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")
'''


# Exception handling ------------------

'''
    The process of responding to unwanted or unexpected events when a computer program runs.
    It deals with these events to avoid the program or system crashing, and without this process, exceptiona would disrupt the normal operation of a program.
    try.....except blocks are used in python to handle errors and exceptions.

'''


a = input("Enter the number: ")
print(f"Multiplication table of {a} is ")

try:
    for i in range(11):
        print(f"{a} X {i} = {int(a)*i}")
except Exception as e:
    print("Sorry")

print("some lines of code")
print("end of the pgm")