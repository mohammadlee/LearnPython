from Person_class import persons,student


for i in range (1,3):
    a=input("enter name:")
    b=input("enter last name:")
    p=persons(a,b)
    print(p.person())
    stu=input("Are you student?Y/N")
    if stu=='Y'or stu=='y':
        id=int(input("enter your id number:"))
        meu=input("enter your meuser:")
        cou=input("enter your course:")
        student=student(a,b,id,meu,cou)
        print(student.student_id())
        print(student.class_measure())
        print(student.class_cours())
    else:
        break



