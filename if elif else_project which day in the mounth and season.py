n=int(input("enter day of you want:"))
if n<0 or n>365 :
    print("the day of years betwwen 1 and 365")
else:
    month=n//31
    if month>6:
        month=6
    n-=month*31
    if n!=0:
        count=n//30
        month+=count+1
        n -= count * 30
    else:
        n=31
    if n==0:
        n=30
        month=month-1
    print("day is",n,"of month",month,sep=" ",end=' ')
    if month==1:
        print(("farvardin"),end=' ')
    elif month==2:
        print(("ordibehaesh"),end=' ')
    elif month==3:
        print(("khordad"),end=' ')
    elif month==4:
        print(("tir"),end=' ')
    elif month==5:
        print(("mordad"),end=' ')
    elif month==6:
        print(("sharivar"),end=' ')
    elif month==7:
        print(("mehr"),end=' ')
    elif month==8:
        print(("aban"),end=' ')
    elif month==9:
        print(("azar"),end=' ')
    elif month==10:
        print(("dey☺"),end=' ')
    elif month==11:
        print(("bahman"),end=' ')
    elif month==12:
        print(("esfand"),end=' ')
    print("of season ",end=' ')
    if month<=3:
        print("bahar")
    elif month<=6 and month>3:
        print("tabestan")
    elif month<=12 and month>6:
        print("zemestan")