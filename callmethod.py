#program to overloadthe__call__method
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,o):
        return self.num* o
x=multi(10)
print(x(5))
