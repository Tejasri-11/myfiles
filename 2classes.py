""" program that has abstarct class to derive 2 classes rectangle and trinagle
from polygon class and write the methods """
class polygon:
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()
class rectangle(polygon):
    def get_data(self):
        self.length=float(input("enter rectangle length:"))
        self.breadth=float(input("enter rectangle breadth:"))
    def area(self):
        return self.length*self.breadth
class triangle(polygon):
    def get_data(self):
        self.base=float(input("enter triangle base:"))
        self.height=float(input("enter triangle height:"))
    def area(self):
        return 0.5* self.base*self.height
r=rectangle()
r.get_data()
print("area of rectangle",r.area())
t=triangle()
t.get_data()
print("area of triangle",t.area())

                                     
        
