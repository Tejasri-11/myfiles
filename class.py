#program to access a class var using a class obj

'''class abc:
    var="teju"
obj = abc()
print(obj.var)'''

#program to acess class member using class obj
'''class abc:
    var="Rakesh"
    def display(self):
        print("he is a waste fellow")#class method
obj=abc()
print(obj.var)
obj.display()'''

#program to illustrate the constructor
#__init__()---method(double underscore)

'''class abc:
    def __init__(self,val):
        print("he is selfish")#in class method
        self.val=val
        print("his value is:",val)
obj=abc(0)'''

#program to differentiate b/w class and obj var
class abc:
    class_var=0#class variable
    def __init__(self,var):
        abc.class_var +=1
        self.var=var#obj variable
        print(" the obj var is:",var)
        print("the class value of c=var",abc.class_var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)


