### Built  in-class attributes
'''1. ._dict_
2. ._doc_
3. ._name_
4. ._bases_'''

class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print('var1 is =',self.var1)
        print('var2 is =',self.var2)
obj=abc(10,12.34)
obj.display()
print('object._dict-',obj.__dict__)
print('object._doc-',obj.__doc__)
print('object._name-',abc.__name__)
print('object._module-',obj.__module__)
print('object._bases-',abc.__bases__)
