"""n=int(input("enter position:"))
a=b=0
for i in range (1,n+1):
    if(i%2!=0):
        a=a+7
else:
            b=b+6
   
if n%2!=0:
    print('{} at accordance {}'.format(n,a-7))

else:
        print('{} at accordance {}'.format(n,a-6))"""

n=int(input("enter range"))
list=[]
for i in range(0,n+1):
    a=2**i
    list.append(a)
    b=3**i
    list.append(b)
print(list)
num=int(input("enter the position: "))
print(list[num-1])

"""n=int(input())
m=n

for i in range (0,n+1):
    print(i**2,end=" ")
    print(i**3,end=" ")
print(m.index[12])"""
    
