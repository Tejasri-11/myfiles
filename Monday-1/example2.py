'''write a program to combine list to a dictionary to form a hash table
input: keys=['name','age','branch']
       values=['ABC','100','aeronautical']
l=input().split()
v=input().split()
ou=zip(l,v)
d=dict(ou)
print(d)'''


""" write a program to store a sparse matrix in a dictonary
ex:
[0,0,0,1,0]
[2,0,0,0,3]
[0,0,0,4,0]"""
a=[[0,0,0,1,0],[2,0,0,0,3],[0,0,0,4,0]]
d={}

for i in range(len(a)):
    for j in range(len(a[i])):
        if(a[i][j]!=0):
            d[i,j]=a[i][j]
                   
print(d)
