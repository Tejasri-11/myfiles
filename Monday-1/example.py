n=int(input())
if(n<=0):
    print("Invalid Input")
    quit()
x=input().split()
x=[int(i) for i in x]
o=[]
e=[]
for i in range(0,n):
    if(x[i]%2==0):
        e.append(x[i])
    else:
        o.append(x[i])
        


x=[]
l=e+o
for i in l:
    print(i,end=" ")
