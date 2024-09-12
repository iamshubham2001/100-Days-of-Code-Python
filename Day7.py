#--------------Tuple-------------------


'''
    Tuples are ordered collection of data items. They store multiple item in a single variable. Tuple items are saperated by commas and enclosed within round brackets ().
    Tuples are unchangeable meaning we can not alter them after creation
'''

'''
tup=(1,2,76,342,32,"green",True)
print(type(tup),tup)
print(tup[0])
print(len(tup))

if 342 in tup:
    print(" yes 342 is present in the tuple")
'''

# Operation of tuples

# Manipulating Tuples

'''
countries = ("spain","Russia","Italy","England","China")
temp=list(countries)
temp.append("India")    # Add
temp.pop(3)             # Remove
temp[2]="Finland"       # Change item
countries=tuple(temp)
print(countries)
#print(temp)
'''

'''
c1 =("Pakistan", " China", "Bangladesh", "Srilanka", "India")
c2 = ("USA","Canada","Argentina","Japan")
countries= c1+c2
print(countries)
'''

'''
    # count()

t1=(1,2,3,4,3,3,2,3,5,7,3)
res=t1.count(3)
res1=t1.index(3,4,8)
print(res)
print(res1)
'''



