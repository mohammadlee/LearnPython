# if ,else
age =20
if age <=20:
    print("your are teen")
else:
    print("your age more the 20")
#and
a=10
b=20
if a>5 and b>15 :
    print("it's ok ")
else:
    print("it's not correct")
#or
a=10
b=20
if a>5 or b>25 :
    print("it's ok ")
else:
    print("it's not correct")
#if elif else
temp= int(input("What is the air temperature?\n"))
if temp<-20  :
    print(" it's so cold and you will be die soon ")
elif -20<temp and temp<0 :
    print("it's cold but you can live ")
elif 0<=temp and temp <15:
    print("it's so good ,you can go to the picnic")
elif  temp<=15 and temp<35:
    print("it's so hot but you can take sun shower")
elif temp<=35 and temp<45:
    print("it's so hot")
elif temp<=45:
    print("You are going to be an omelette")
else:
    print("it's not correct")
#Nested If
age =int(input("Enter your age"))
if age >18 and age <40 :
    print("you are young")
    if age < 18 and age<25:
        print("you are student")
    else :
        print("you are young but  maybe you are not student")
else:
    print("you are adult")
