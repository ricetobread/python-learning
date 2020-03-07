from random import randint

#list of possibility
game=["Rock","Paper","Scissor"]

#assign random play to computer
computer=game[randint(0,2)]

#set player to False
player=False

while player==False:
    player=input("Rock/Papers/Scissor=")
    if player==computer:
        print("It's a Draw!")
    if player=="Rock":
        if computer=="Paper":
            print("You lose!",computer, "covers",player)
        else:
            print("You win!",player, "smashed",computer)
    if player=="Paper":
        if computer=="Scissor":
            print("You lose!",computer, "cut",player)
        else:
            print("You win!",player, "covers",computer)
    if player=="Scissor":
        if computer=="Rock":
            print("You lose!",computer, "smashed",player)
        else:
            print("You win!",player, "cut",computer)
    else:
        print("Check your spelling,bro. Perhaps you forgot a letter?")

        player=False
        computer=game[randint(0,2)]