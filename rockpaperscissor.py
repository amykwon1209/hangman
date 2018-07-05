from random import *
#player chooses rock, paper, scissor
totalattempt = 10
cscore = 0
pscore = 0
while totalattempt > 0:
    computerList = ["rock", "paper", "scissor"]
    computer = choice(computerList)
    computer = computer.lower()

    for idx in range(0, 2): print(" ")
    player = input("rock, paper, or scissor? ")
    player = player.lower()
    w = "You Won!"
    l = "You Lose!"
    if (player.isalpha() == False):
        print("That's not a word!")
    elif (player == "stop"):
        print("Goodbye my friend!")
        totalattempt = - 10
    elif (player == "rock" or player == "paper" or player == "scissor"):
        print(" ")
        print("----------------------------------")
        print("rock paper scissor shoot!")
        print(" ")
        print("Computer" + "      " + "Player")
        print("--------" + "      " + "------")
        print("  " + computer + "  vs  " + player + "  ")
        print(" ")

        if (player == computer):
            print("You are a tie!")
            cscore += 1
            pscore += 1
        elif (player == "rock"):
            if (computer == "scissor"): print(w); pscore += 1
            elif (computer == "paper"): print(l); cscore += 1
        elif (player == "scissor"):
            if (computer == "paper"): print(w); pscore += 1
            elif (computer == "rock"): print(l); cscore += 1
        elif (player == "paper"):
            if (computer == "scissor"): print(l); cscore += 1
            elif (computer == "rock"): print(w); pscore += 1
        print(" ")
        print("Computer score: " + str(cscore) + "           " + "Player score: " + str(pscore))
        print(" ")
        print("=================================================================")
        totalattempt -= 1

    else:
        print("That's not an option!")
        print("Try again!")

if (totalattempt == 0):
    for i in range(2): print(" ")
    if (pscore > cscore):
        print("CONGRATULATIONS! YOU WON THE GAME!")
    elif (cscore > pscore):
        print("I'M SORRY! YOU LOST THE GAME!")
    elif (pscore == cscore):
        print("YAY! YOU ARE A TIE")
    for i in range(2): print(" ")
