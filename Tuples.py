#Tuple
t1=("black","green","white","yellow","orange")
print(t1)
print(type(t1))
l=list(t1)
print(l)
print(len(t1))
#in tuple you cant append new iteam
# t1.append("purple")
# print(t1)
#but you must cast tuple
l.append("purple")
print(l)
t1=tuple(l)
print(t1)
t2=("orange","apple","banana","raspery","cherry")
t3=t2+t1
print(t3)
print(t3.count("orange"))
print(t3.index("apple"))
