#diamond or rhombus pattern
'''rows = int(input())
i=1
while i<=rows:
    j=rows
    while j>i:
        print(" ",end= " ")
        j-=1
    print("*",end=" ")
    k=1
    while k<2*(i-1):
        print(' ',end= ' ')
        k+=1
    if i==1:
        print()
    else:
        print("*")
    i+=1
i=rows -1
while i>=1:
    j=rows
    while j>i:
        print(' ',end=' ')
        j-=1
    print('*',end=' ')
    k=1
    while k<2*(i-1):
        print(' ',end=' ')
        k+=1
    if(i==1):
        print()
    else:
        print("*")
    i-=1'''
#with for loop
rows=5
k=2*rows-2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")
k=rows-2
for i in range(rows,-1,-1):
    for j in range(k,0,-1):
        print(end=" ")
    k=k+1
    for j in range (0,i+1):
        print("*",end=" ")
    print(" ")    
