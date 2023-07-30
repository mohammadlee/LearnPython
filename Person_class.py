class persons:
    def __init__(self,name,lastname):
        self.name=str(name)
        self.lastname=str(lastname)
    def person(self):
        print("he/she is",self.name,self.lastname,sep=' ',end='\n')

class student (persons):
    def __init__(self,name,lastname, id,measure,course):
        super().__init__(name, lastname)
        self.id=int(id)
        self.measure=str(measure)
        self.course=str(course)
    def student_id(self):
        print("he is ",self.lastname,"and this is ",self.id,sep=' ',end='\n')
    def class_measure(self):
        print("he's measure",self.measure,sep=' ',end='\n')
    def class_cours(self):
        print("he's cours ",self.course,sep='',end='\n')