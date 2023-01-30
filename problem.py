''' there is a jar full of candies for sale at a mall counter. Jar has the capacity N, that is jar can contain maximum N candies
when jar is full. At any point of time. Jar can have M no of candies where M<=N candies are served to customers. Jar is never
remain empty as when last k candies are left. Jar if refilled with new candies in such a way that jar get full

write a code to implement above scenerio. Display JAR at counter with available no of candies.Input should be the no of candies
one customer can order at point of time.Update the JAR after each purchase and display JAR at counter.

output should give number of candies sold and updated no of candies in JAR

if input is more than candies in JAR, return:"INVALID INPUT" given,
N=10,where N is num of candies available
k=<5, where k is the no of minimum candies that must be inside jar ever.

example1:(N=10,k=<5)
input value
 3
output value
 no of candies sold:3
 no of candies available:7 '''
n=10
x=int(input())
 
if (x==0):
   
    print("invalid input")
    print("availabe:",n)
elif (x<=5):
    a=n-x
    print("sold",x)
    print("available",a)
else:
    print("invalid input")
 
