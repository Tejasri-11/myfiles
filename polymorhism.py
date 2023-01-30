#encapsulating
class pub:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def Num(self):
        print("roll num is",self.num)
obj=pub("harry",299)
obj.Num()
