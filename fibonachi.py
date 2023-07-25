n= int(input("enter number:"))
x1=0
x2=1
x3=0
if (n==1):
    print(x1)
elif (n==2):
    print(x1,"\t",x2)
else:
    print(x1)
    for i in range(n):
        x3=x1+x2
        print(x3)
        x1=x2
        x2=x3