n= int(input("enter a number:"))
for i in range(n):
    if (i%2==0):
        print("this even",i,sep=" ",end="\n")
    else:
        print("it's odd",i,sep=" ",end="\n")