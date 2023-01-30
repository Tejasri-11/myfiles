'''n=int(input())
d={}
for i in range(n):
    x=input("username:")
    y=input("password:")
    d[x]=y
print(d)'''


#using array
'''n=int(input())
arr=[]
for i in range(n):
    username=input("Username:")
    password=input("password:")
    arr.append({username,password})
print(arr)'''
#password incorret or correct
d={}
l=[]
n=int(input("enter the number of users:"))
for i in range(n):
    k=input("enter user name:")
    y=input("enter password:")
    l.append(k)
    d[k]=y
    print(d)
u=input("enter username:")
p=input("Enter password:")
if u in l:
    if d[u]==p:
        print("Login Successfull")
    else:
        print("Wrong password")
else:
    print("Wrong username")

