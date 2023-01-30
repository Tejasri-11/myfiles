size=int(input("enter the size:"))
for i in range(1,2*size):
         for j in range(1,2*size):
              if i==size or j==size:
                 print('*', end=' ')
              else:
                 print(' ', end=' ')
         print()
