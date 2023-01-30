#program to over-ride get-item and set-item methods
class mylist:
    def __init__(self,list):
        self.list=list
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,num):
        self.list[index]=num
    def __len__(self):
        return len(self.list)
    def display(self):
        print(self.list)
l=mylist([1,2,3,4])
print("list is :")
l.display()
index=int(input("enter the index of the list:"))
print(l[index])
num=int(input("enter the position uh want:"))
l[index]=num
l.display()
print("the length of list is:",len(l))
