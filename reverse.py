'''num=123

while(num!=0):
    temp=num%10
    num=num//10
    print(temp,end=" ")'''
#sir code
""" num=1234
n_string=str(num)
r_num="".join(reversed(n_string))
print("reversed:"r_num)"""
#another method(recursive)
def reverse(n):
        if (len(n)==0):
            return n
        return reverse(n[1:]) +n[0]
num=1234
n_string=str(num)
r_num=reverse(n_string)
print(r_num)
