#to visualize inheritance flow
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name)
        print("age is",self.age)
class teacher(person):
        def __init__(self,name,age,exp,rarea):
            person.__init__(self,name,age)
            self.exp=exp
            self.rarea=rarea
        def displaydata(self):
            person.display(self)
            print("experience is:",self.exp)
            print("reqasearch area",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("----------teacher class--------")
T=teacher("rakesh",43,20,"jss")
T.displaydata()
print("----------student class---------")
S=student('teju',20,'B.E',78)
S.displaydata()
