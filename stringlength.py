#string length
#method by sum
'''def ls(string):
    return sum(1 for i in string)
string = 'india'
print(ls(string))'''
'''#counter method
def ls(str):
    c=0
for i in str:
    c+=1
    return c
str="SRU"
print(ls(str))'''
#join and count
def ls(str):
       if not str:
           return 0
        else:
    r_str='py'
     return ((r_str).join(str).c(r_str)+1)

    
