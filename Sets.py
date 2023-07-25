s={"mohammad","ali","javad","akbar"}
print(s)
s.add("yasin")
print(s)
s1={"sara","mahsa","atosa"}
#you can't add list set tuple
# s.add(s1)
# print(s)
#but you can update
s.update(s1)
print(s)
#remove
s1.remove("sara")
print(s1)
s1.discard("atosa")
print(s1)
s1.clear()
print(s1)
s2={1,2,3,4}
s3=s.union(s2)
print(s3)
s4={3,4,5,6}
print(s2.symmetric_difference(s4))
s4={3,4,5,6,7}
print(s2.symmetric_difference_update(s4))
print(s1.issuperset(s4))
print(s4.issuperset(s2))
s5={1,2,3}
print(s5.issuperset(s1))
print(s4.isdisjoint(s5))
print(s4.intersection(s2))