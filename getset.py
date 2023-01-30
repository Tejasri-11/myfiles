'''__repr__ ----syntax report of obj
__cmp__-----compare 2 class objs
__len__------length(obj)
__call__it acts like a func to call its instances
__lt__,__le__,__eq__,__ne__,__gt__,__ge__------cmp of 2 objects
__iter__ -----iteration over an obj
__getitem__---used for indexing
eg:
gs:def__getitem__(self,var/key)
set item assign an item to indexed value'''

#program for get and set items in the list
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])
