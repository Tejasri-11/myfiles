#program to invoke __init__ in multiple inheritance
class base1(object):
    def __init__(self):
        print("base class1")
class base2(object):
    def __init__(self):
        print("base class 1")
class Derived(base1,base2):
    pass
D=Derived()
