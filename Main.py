# Python program for Snake, Water, Gun game (Player vs Player)
arr=["Snake","Gun","Water"]
player1=input("Enter any word : ")
player2=input("Enter any word : ")        
if player1==player2:
    print("Tie")
elif player1=="Snake" and player2=="Water":
    print("Player1 won")
elif player1=="Snake" and player2=="Gun":
    print("Player2 won")
elif player1=="Water" and player2=="Snake":
    print("Player2 won")
elif player1=="Water" and player2=="Gun":
    print("Player1 won")
elif player1=="Gun" and player2=="Snake":
    print("Player1 won")
elif player1=="Gun" and player2=="Water":
    print("Player2 won")
else:
    print("Please only provide input of rock,paper and scissor")

# Python program for Snake, Water, Gun game (Player vs Computer)
import random
options=[-1,0,1]
computer=random.choice(options)
print(computer)
user=input("Enter the word : ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"s",-1:"w",0:"g"}
you=youdict[user]
print(f"Your choice {reversedict[you]}\n Computer choice {reversedict[computer]}")
if computer==you:
    print("Tie")
elif computer==-1 and you==0:
    print("computer won")
elif computer==-1 and you==1:
    print("You won")
elif computer==0 and you==-1:
    print("you won")
elif computer==0 and you==1:
    print("computer won")
elif computer==1 and you==-1:
    print("computer won")
elif computer==1 and you==0:
    print("you won")
else:
    print("Please only provide input of s,w and g")
