# this is comment you can use (ctrl + /) in windows
# bool(true,false) , int(..,-1,0,1,2,...) , str("word and all of symbol"), float(-1.0001,0,1.0001,0000)
b=True
print(b)
print(b is False)
print(b is True)
print(b is not False)
# show type of var
print(type(b)) # bool
#int
i=10
print(type(i))
print(i+10) #20
print(i-22) #-12
print(i*3)  #30
print(i/5)  #2
#print(i++) Error we don't have it
i=i+1
print(i)#11
i+=1
print(i)#12
a=10
b=10
print(a+b)
c=a+b
print(c)
# a=str(a)
# print(a,b)
a=-100
print(abs(a))
a=20
b=58
c=89
print(max(a, b, c))
print(min(a, b, c))
#str
p='mohammad is 30'
print(type(p))
print(p.lower())
print(p.upper())
print(p.replace("m", "w"))
print(len(p))
print(p.index("d"))
print(p[4])
print(p.split("is"))
print(p.capitalize())
print(p.casefold())
#input for insert something in programme
name= input("what is your name? \n")
print("your name is "+ name)
age = int(input("how old are you ?\n"))
print("your are ", age)
height=float(input("what is your height?\n"))
print("your height is ", height)
