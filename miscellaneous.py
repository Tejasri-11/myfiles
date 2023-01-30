#special or miscellaneous functions in overloading
class number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self.num)
    def __oct__(self):
        return oct(self.num)
    def __setitem__(self,num):
        self.num=num
n=number(-14)
print('n is =',n.display())
print('abs(n) is =',abs(n))
n=abs(n)
print('converting to float',float(n))
print('converting to hexa',hex(n))
print('converting to octa',oct(n))
