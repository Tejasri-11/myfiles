class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var- obj.var
obj=abc('abcd',10)
print('the value stored in obj is',repr(obj))
print('the length of the name stored in obj',len(obj))
obj1=abc('efgh',1)
val=obj.__cmp__ (obj1)
if val==0:
    print("both values are equal")
elif val==1:
    print('1st value is less than second')
else:
    print('2nd value is less than 1st')
