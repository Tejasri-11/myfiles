#program to find the exp(x,y) using recursion function
'''def expo(x,y):
    if y==0:
        return 1
    else:
        return(x*expo(x,y-1))
n=int(input())
m=int(input())
print("result=",expo(n,m))'''

#program for fibonociee series:
'''def fibno(x):
    if x<0:
        print("incoreect input")
    elif x==0:
        return 0
    elif x==1 or x==2:
        return 1
    else:
        return fibno(x-1)+fibno(x-2)
n=int (input())
print (fibno(n))'''

#with recursion
'''def  fibbo(n):
    if n<2:
        return 1
    return (fibbo(n-1)+fibbo(n-2))
n=int(input())
for i in range(n):
    print("fibbonaci(",i,")=",fibbo(i))'''
#tower of hanoi
'''def Tower(n , s, d, i):           
    if n == 1:
        print("Move disc 1 from pole",s,"to pole",d)
        return
    Tower(n-1, s, i, d)
    print("Move disc",n,"from pole",s,"to pole",d)
    Tower(n-1, i, d, s)

n =int(input("enter no of disks:"))
Tower(n, 'A', 'C', 'B')'''

#tower of hanoi iteration with 4disks and 3 poles
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print(a,b,c)
hanoi(len(a),a,b,c)
        
    



        

