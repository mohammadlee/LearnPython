def car():
    print("this is a car")
def car1(name,color,year):
    print(name, " is ",color," from ",year)
def salme():
    return salme
def team(*player):
    print("we have ",player[:])
def hotel(name,lastname,room=" room not select"):
    print("mr/mrs ",name,lastname, room,sep=' ',end=' ')
def hospital(nameH,lastnamH,idH):
    a=[]
    b=[]
    c=[]
    a=nameH.copy()
    b=lastnameH.copy()
    c=idH.copy()
    print("your name is",a[0],"your last name is ",b[0],"number of room is",c[0],sep=' ',end='\n')
print(salme())
print(car())
print(car1("benz", "red", 1998))
player=[]
for i in range(0,1):
    player.append(input("enter player name:"))
print(team(player))
name=input("enter your name:")
lastname=input("enter your lastname:")
room=int(input("enter your room number:"))
hotel(name,lastname)
n=int(input("enter number of sick:"))
nameH=[]
lastnameH=[]
idH=[]
for i in range(0,n):
    nameH.append(input("enter name of the sick:"))
    lastnameH.append(input("enter last name of sick:"))
    idH.append(input("enter id of sick:"))
hospital(nameH,lastnameH,idH)