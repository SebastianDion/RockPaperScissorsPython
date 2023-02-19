from random import randint
import sys

print("Welcome to Rock,Paper,Scissor....")
print("press any key to start and type 'end' to terminate")

buffer =input()

listOption =["Rock", "Paper", "Scissor"]
Score=0
Bot=listOption[randint(0,2)]
Player1=False

while Player1 == False:
    print("Score:",Score)
    Player1 =input("Rock,Paper,Scissors?")
    if Player1 == Bot:
        print("Tie, go again!")
    elif Player1 == "Rock":
        if Bot == "Paper":
            print("You lose!", Bot, "Covers", Player1)
        else:
            print("You win!", Player1, "smashes", Bot)
            Score+=1
    elif Player1 == "Paper":
        if Bot == "Scissors":
            print("You lose!", Bot, "cut", Player1)
        else:
            print("You win!", Player1, "covers", Bot)
            Score+=1
    elif Player1 == "Scissors":
        if Bot == "Rock":
            print("You lose...", Bot, "smashes", Player1)
        else:
            print("You win!", Player1, "cut", Bot)
            Score+=1
    elif Player1 == "end":
        print("Thank you for playing Rock,Paper,Scissors")
        sys.exit()
    else:
        print("Invalid Input,try again")
    Player1 = False
    Bot= listOption[randint(0,2)]



