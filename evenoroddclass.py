'''class number:
    even=0#default value
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
num=int(input())
obj=number()
obj.even_odd(num)'''

#print odd and even seperately
class number:
    even=[]
    odd=[]
    
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1=Number(22)
n2=Number(33)
n3=Number(44)
n4=Number(55)
n5=Number(66)
n6=Number(77)
print("even numbers:",Number.even)
print("odd number:",Number.odd)
            
        
