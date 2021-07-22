from random import choice
print("Welcome to the rock-paper-scissor game")
print("enter player name")
name=input()
print("enter number of rounds to play")
n=int(input())
u=0             
c=0             
while(n):
    print("enter r for rock,p for paper, s for scissor")
    user=input()
    print(name,"entered ",user)
    comp=choice("rps")
    print("computer entered ",comp)
    if(user=='r'and comp=='p'):
        print("computer wins this round")
        c+=1
    elif(user=='r'and comp=='s'):
        print(name,"wins this round")
        u+=1
    elif(user=='p' and comp=='r'):
        print(name,"wins this round")
        u+=1
    elif(user=='p' and comp=='s'):
        print("computer wins this round")
        c+=1
    elif(user=='s' and comp=='r'):
        print("computer wins this round")
        c+=1
    elif(user=='s'and comp=='p'):
        print(name,"wins this round")
        u+=1
    else:
        print("This is round is a tie")
    n-=1
print("the final score is:")
print(name+":",u,"\t","Computer:",c)
if(u>c):
    print(name,"wins the game")
elif(u<c):
    print("computer wins the game")
else:
    print("the game ends in a tie")