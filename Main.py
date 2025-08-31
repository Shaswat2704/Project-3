arr=["Rock","Paper","Scissor"]
player1=input("Enter any word : ")
player2=input("Enter any word : ")        
if player1==player2:
    print("Tie")
elif player1=="Rock" and player2=="Scissor":
    print("Player1 won")
elif player1=="Rock" and player2=="Paper":
    print("Player2 won")
elif player1=="Paper" and player2=="Scissor":
    print("Player2 won")
elif player1=="Paper" and player2=="Rock":
    print("Player1 won")
elif player1=="Scissor" and player2=="Paper":
    print("Player1 won")
elif player1=="Scissor" and player2=="Rock":
    print("Player2 won")
else:
    print("Please only provide input of rock,paper and scissor")