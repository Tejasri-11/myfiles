cname=input("enter any name:")
pname=input("enter product name:")
qty=int(input("enter no.of products:"))
prate=int(input("enter rate"))
ta=prate*qty
if(qty>=10):
             da=ta*5/100
             
else:
            da=ta*2/100
            
pa=ta-da
print("cname:",cname)
print("pname:",pname)
print("qty:",qty)
print("prate:",prate)
print("da:",da)
print("ta:",ta)
print("pa:",pa)
