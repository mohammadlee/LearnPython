#list
names=["ali","mohammad","ali","amin","ehsen","pouria","mohamamd","navid","mohammad"]
print(type(names))
print(names)
print(names[0])
print(names[1:2])
print(names[1:])
print(names[:2])
print(names[0:6:2])
print(names[-1])
print(names[:-1])
print(len(names))
print(names.count("mohammad"))
names.insert(9,"mohsen")
print(names)
names.remove("ali")
print(names)
names.append("mohamamdreza")
print(names)
print(names.pop())
print(names)
names.sort()
print(names)
names.reverse()
print(names)
l1=sorted(names)
print(l1)
l2=["sara","parisa","akram", " jahaleh"]
print(l1+l2)
l1.append(l2)
print(l1)
del l1
print (l1)# error because , it's not exist

