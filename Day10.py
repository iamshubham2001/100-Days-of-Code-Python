#---------Set method in Python-----------


'''
s1={1,2,3,4,5}
s2={6,7,5,8}
print(s1.union(s2))     # Union
s1.update(s2)           # update
print(s1,s2)
'''

cities1={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=(cities1.union(cities2))
print(cities3)
cities4=(cities1.intersection(cities2))   # intersection
print(cities4)

# symmetric Difference

cities5=(cities1.symmetric_difference(cities2))
print(cities5)