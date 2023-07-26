for i in range(10):
    for j in range(i+1):
        print(" * ",end='')
    print()

print("######################################")
for i in range(5):
    print(' * ' * (i + 1))
print("######################################")
n=int(input("enter number:"))
for i in range(1,n+1):
    print((n-i)*' '+ (2*i - 1)*'*')
print("######################################")
for i in range(10,1,-1):
    print(' * ' * (i - 1))
print("######################################")
n=int(input("enter number:"))
for i in range(n):
    for j in range(n):
        print(" * ",end="")
    print()
print("######################################")
a=int(input("enter wigth number:"))
b=int(input("enter hegth number:"))
for i in range(a):
    for j in range(b):
        print(" * ",end="")
    print()
print("######################################")
n=int(input("enter number:"))
for i in range(1,n+1):
    print((n-i)*' '+ (2*i - 1)*'*')
for i in range(1,n+1):
    print((i)*' '+(-2*i+(2*n-1))*'*')