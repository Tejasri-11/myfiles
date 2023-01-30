#program to demo access of var in inner and outter function
'''def outer_fun():#2nd step
    outer_var=11#3rd step
    def inner_fun():#5th step
        inner_var=22#6th
        
        print("inner variable",inner_var)#7th
    inner_fun()#4th step
    print("outer variable",outer_var)#8th
outer_fun()#1st step'''

#writing a function and return its cubation format
'''def cube(x):
    return(x*x*x)
num=10
result=cube(num)#cube of (10)
print("cube of ",num,"=",result)'''

#writing a function for mismatch parameter
'''def abc(x):
    print("hiiiii",x)
#abc(5, 5)gets error because one varaibale gives only one parameter
abc(5)'''

def fun(i):
    print("orange",i)
j=10
fun(j)#iandj differnt parameters but the results same

        
