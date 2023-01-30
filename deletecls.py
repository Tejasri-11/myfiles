#delete method syntax: __del__
class abc():
    class_var=0
    def __init__(self,var):
        abc.class_var +=1
        self.var=var
        print("the obj value is:",var)
        print("the class value is:",abc.class_var)
    def __del__(self):
        abc.class_var -=1
        print("obj with value  %d is going out of scope",self.var)
obj1=abc(11)
obj2=abc(22)
obj3=abc(33)
del obj1
del obj2
del obj3

    
