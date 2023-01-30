#program to call constructor of a base class from super
class base1(object):
    def __init__(self):
        print('base class 1')
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print('base class 2')
class derived(base1,base2):
     def __init__(self):
        super(derived,self).__init__()
        print('derived class')
D=derived()
