#---------Set method in Python-----------


'''
s1={1,2,3,4,5}
s2={6,7,5,8}
print(s1.union(s2))     # Union
s1.update(s2)           # update
print(s1,s2)
'''


'''
cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=(cities1.union(cities2))
print(cities3)
cities4=(cities1.intersection(cities2))   # intersection
print(cities4)

# symmetric_Difference

cities5=(cities1.symmetric_difference(cities2))
print(cities5)

# isdisjoint()
cities6=(cities1.isdisjoint(cities2))
print(cities6)

# issuperset()

print(cities1.issubset(cities2))
print(cities1.add("Bihar"))

# Remove---->>Discard
# del cities
# clear cities
'''

info={"shubham","raju",19,False,5.9,"chintu"}
if "shubham" in info:
    print("yes")
else:
    print("no")