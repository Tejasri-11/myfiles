import random
print("*****************ROCK PAPER SCISSORS*****************\n\n")
i=0
j=0
no=0
while(no!=5):
    print("ROUND ",no+1);
    print()
    n=input("Enter your choice:")
    l=["Rock","Paper","Scissors"]
    s=random.choice(l)
    print("Computer choice",s)
    if n=="Rock" or n=="rock":
        if s=="Scissors" or s=="scissors":
            print("Player won")
            i+=1
        elif s=="Rock" or s=="rock":
            print("DRAW")
        else:
            print("Computer won")
            j+=1
    elif n=="Scissors" or n=="scissors":
        if s=="Paper" or s=="paper":
            print("Player won")
            i+=1
        elif s=="Scissors" or s=="scissors":
            print("DRAW")
        else:
            print("Computer won")
            j+=1
    elif n=="Paper" or n=="paper":
        if s=="Rock" or s=="rock":
            print("Player won")
            i+=1
        elif s=="Paper" or s=="paper":
            print("DRAW")
        else:
            print("Computer won")
            j+=1
    else:
        print("INVALID INPUT")
    no+=1
print("\n\n")
if(i>j):
    print("Player won the match")
else:
    print("Computer won the match")
