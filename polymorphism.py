#program to interview polymorhism on a complex number
class complex():
    def __init__(self):
        self.real=0
        self.img=0
    def setValue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        temp = complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=complex()
c1.setValue(1,2)
c2=complex()
c2.setValue(3,4)
c3=c1+c2
print("result is:")
c3.display()
    
   
