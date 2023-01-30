#swapping numbers
'''def swap(a,b):
    a,b=b,a
    print("after swap;")
    print("a= ",a)
    print("b= ",b)
a=int(input("a="))
b=int(input("b="))
print("before swap")
print("a= ",a)
print("b= ",b)
swap(a,b)'''

#program to write full name of a person
'''def name(str1,str2):
    s=' '
    n=str1+s+str2
    return n
print(name("tejasri","p"))'''

#program for even or odd
'''def eo(n):
    if a%2==0:
        return 1
    else:
        return -1
a=int(input())
flag=eo(a)
if flag==1:
    print("even")
else:
    print("odd")'''
    
''' write a program to claculate st.suppose the customer is a senior citizen.
he is being offered by 12% ROI;for all other customer ,the ROI 10%.'''
'''p=200
r=3

age=int(input())
if age>=60:
    ROI=0.12
else:
    ROI=0.01
si=p*r*ROI/100
print(si)'''

#factorial number:
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input())
print (fact(n))

        


