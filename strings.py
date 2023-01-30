"""str="hi"
print(str.capitalize())
#$$$$$hi$$$$$$
str="hi"
print(str.center(10,'$'))"""
#
"""str="ll"
substr="hehellhehell"
print(substr.count(str,0,len(substr)))"""
#
"""str="she is my sister"
print(str.find("sister",0,len(str)))"""
#syntax for left justificatio:
#ljust(width[,fillchar])
"""str="hi"
print(str.ljust(20,'^'))"""
#zfill(width)
'''str="6"
print(str.zfill(4))'''
#title (whole sentence starts with capital letter)
'''str="I Am a Good Girl"
print(str.title())
print(str.swapcase())#opposite of title
print(list(enumerate(str)))#index values will be shown'''
#spacing between each letter in a sentence by using for
str="very good girl"
for i  in str:
    print(i,end=" ")


