num=int(input())
n=num
s=0
while(num!=0):
    temp=num%10
    s=s+temp
    num=num//10
print(s)
d=n//s
print(d)
if num%s == 0:
    print("nivens number")
else:
        print("not nivens number")
    
