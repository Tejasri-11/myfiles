class Node:
    def __init__(self,num):
        self.num =num
        self.next=None
class Llist:
    def __init__(self):
        self.head=None
    def push(self, newnum):
        newnum=Node(newnum)
        newnum.next=self.head
        self.head=newnode
    def insertnext(self,prenode,newnode):
        if prenode is None:
            print('the previous node')
            return
        newnode=Node(newnum)
        newnode.next=prenode.next
        prenode.next=newnode
    def append(self,newnum):
        newnode=Node(newnum)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=newnode
    def printnum(self):
        t=self.head
        while(t):
            print(t.num)
            t=t.next
if __name__=='__main__':
    l1=Llist()
    l1.append(1)
    l1.append(3)
    l1.append(5)
    l1.append(8)
    print(l1.printnum())
