# check if 2 strings match where one string contains wildcard char
def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return true
    if n>1 and a[0]=='*' and m==0:
        return false
    if (n>1 and a[0]=='?')or(n!=0and m!=0 and a[0]==b[0]):
        return solve(a[1:],b[1:])
    if n!=0and a[0]=='*':
        return solve (a[1:],b)or solve (a,b[1:])
        return false
x=str(input("enter str with char"))
y=str(input("enter str for match"))
print("with wild char:",x)
print("without wild char:",y)
print(solve(x,y))
