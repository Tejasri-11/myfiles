def happ(num):
   rem=0
   sum=0
   while(num>0):
       rem=num%10
       sum=sum+(rem*rem)
       num=num//10
       return sum
num=97
result=num
while(result!=1 and result!=4):
        result = happ(result)
if result == 1:
            print("happy")
else:
                print("not happy")
    
