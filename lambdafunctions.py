#lambda functions
'''addition=lambda x,y,z:x+y+z
print("sum=",addition(10,20,30))'''
'''
1.lambda function has no names
2.it can take n no of attributes
3.it can only return one value
4.lambda fun cannot access global variables
5.cannot access var other than their parameter list
6.cannot contain multi parameters
7.does not have explicit return stmts'''
#program to find smaller number by lambda
'''def small(a,b):
    if(a<b):
        return a
    else:
        return b
add= lambda x,y:x+y
diff= lambda x,y:x-y
print("smaller of two no:",small(add(-3,-2),diff(-1,2)))'''


#increment function
'''def increment(y):
    return(lambda x : x+1)(y)
a=100
print("a=",a)
print("a after incrementing:")
b=increment(a)
print(b)'''

#program to pass a lambda fun as an fun arg
def fun(f,n):
    print(f(n))#twice(4)
twice= lambda x :x*2
triple= lambda x: x*3
fun(twice,4)
fun(triple,3)

    
