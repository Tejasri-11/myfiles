#basic pattern
#mirror  image pattern
#symmetrical pattern
#choice pattern
#anti pattern\hallow pattern
""" rignt angle triangle"""
'''n=int(input())
i=1
t=0
while i<=n:
    j=1
    while j<=i:
        print("*",end=" ")
        t=t+1
        j=j+1
    i=i+1
    print()'''
#another method with for
'''rows=int(input())
for i in range (rows):
    for j in range(i+1):
        print("*",end=" ")#for numbers print(j+1,end=" ")
    print("\n")'''
        
