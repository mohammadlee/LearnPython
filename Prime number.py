n= int(input("enter number:"))
for i in range(n) :
    if(i==1):
        pass
    elif(  i==2 or i==3 or i==5 or i==7):
        print(i,"\t")
    elif(i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0):
        print(i,"\t")
    else:
       pass