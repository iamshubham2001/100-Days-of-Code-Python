#---------List-----------


'''
    -> Lists are ordered collection iof data items
    -> They stored multiple items in a single variable. 
    -> List item are saperated by commas and enclosed within square brackets [].
    -. Lists are changable meaning we can alter them after creation.
'''

'''  
l=[3,4,5]
print(l)
print(type(l))
'''

'''
marks=[3,5,6]
print(marks)
print(marks[0])
marks.append(4)
print(marks)
'''

'''
marks=[3,4,5,1,7]
print(marks[-3])   # negative index
print(marks[len(marks)-3])  #positive index
print(marks[5-3])  #positive index
print(marks[2])   #positive index
'''

'''
marks=[3,4,5,1,7,"Harry","Shubham",23,21]
print(len(marks))
print(marks[1:8:2])
if 7 in marks:
    print("yes")
else:
    print("no")
'''


'''
--> same thing applies for string as well!

if "arry" in "harry":
    print("yes")
'''

# List comprehension
'''
    used for creating new lists from other iterables like lists, tuples,dictionaries,sets,and even in arrays and strings.
'''

'''
lst = [i*i for i in range(4)]
print(lst)


lst = [i*i for i in range(10) if i%2==0]
print(lst)
'''

# list methods

'''
# append()
l = [1,2,4,7,6]
print(l)
l.append(3)
#print(l)

# sort ()
l.sort()
#print(l)

# reverse()
l.sort(reverse=True)
#print(l)
l.reverse()
#print(l)


# index
print(l.index(1)) 

#count
print(l.count(4))


# copy()

l= [11,33,44,23,12,1,7]
print(l)
m = l.copy()
m[0]=0
print(m)


# insert()
l= [11,33,44,23,12,1,7]
print(l)
l.insert(1,899)
print(l)


#extent()

l= [11,33,44,23,12,1,7]
print(l)
m=[25,56,32,43]
l.extend(m)
print(l)
k=l+m
print(k)
'''