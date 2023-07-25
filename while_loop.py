i=1
while i<=10:
    print(i)
    i+=1
i=0
while i<=20:
    if(i%2==0):
        print(i)
    else:
        print("odd number")
    i+=1

n=int(input("enter number:"))
sum=0
while n>0:
    sum+=n%10
    n=n//10
print("sum of number is ",sum)
n=int(input("enter numer:"))
reverse=0
while n>0:
    reverse=reverse*10+n%10
    n=n//10
print("reverse is", reverse)

n=int(input("enter numer:"))
m=n
reverse=0
while n>0:
    reverse=reverse*10+n%10
    n=n//10
if m==n:
    print("yes")
else:
    print("no")
print("reverse is", reverse)
n=int(input("enter number:"))
sum=0
i=0
while i<5:
    x=0
    x=int(input("enter number:"))
    if x<0:
        print("it's negative")
        break
    elif 0<x:
         sum+=x
    i+=1
print("sum is",sum)

