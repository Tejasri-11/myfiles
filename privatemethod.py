'''class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this from class method,var=",self.__var)
obj=abc(10)
obj._abc__display()'''


#to call a class method form another method of same class
'''class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print('var is =',self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj=abc(10)
obj.add_2()'''
    
#program to show how a class method calls a function which is defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print('var is=',self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=abc(10)
obj.display()
obj.modify()
obj.display()
