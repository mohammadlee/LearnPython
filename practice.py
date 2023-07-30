for i in range(1,7):
    for j in range(i):
        print(i,end=' ')
    print('')
n=int(input("enter number:"))
for i in range(1,n+1):
        print((n-i)*' '+ (2*i - 1)* str(i))
print("##########################################")
for n in range(i+1,1):
    print((i)*' '+(-2*i+(2*n-1))*str(i))
for i in range(1,n+1):
    print((i)*' '+(-2*i+(2*n-1))*'*')