#function-space is allocated in the memory allocation
""" function is into two parts
1.function header
2.function body
syntax: def fun_name(var1,var2,.....):
documentation string
statement block
return[expression/value]
#no arguments -no return values
example:"""
"""def fun():#calee
    for i in range(10):
        print("abcde")
fun()#caller"""
#arguments passed with return values
#example:
"""def add(x,y):#function to add 2 numbers
    return x+y
a=10
b=20
operation=add#function name assigned to a variable
print(operation(a,b))#function calling"""
#global variable
'''var1="hi"
def abc():
    global var2
    var2="goodmorning"
    print("in the function var1 is-",var1)
abc()
print("outside function is var2-",var2)
#variable
print("var1 is-",var1)'''
#modifying global variable
var1="hi"
def abc():
    global var1
    var1="goodmorning"
    print("in the function var1 is-",var1)
abc()
print("outside function is var2-",var1)
#variable
print("var1 is-",var1)
var1="verygood"
print("outside function after modify-",var1)

