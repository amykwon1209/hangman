from random import *
# --- Define your functions below! ---
def space():
    print(" ")
def introduction(name):
    print("Chatbot: Hi, " + name.capitalize() + ". Nice to meet you!")
def options(name, answer):
    answer_list = ["Can you repeat that?", "I'm really good at guessing!",
                    "Ask me what my age is!", "Do you think I have a friend?",
                    "-o-;", "Let me google it, give me a second",
                    "Do you think I'm smart?"]
    if (answer == "hi" or "hello" in answer):
        print(who("Hello there!"))
    elif ("thank you" in answer or "thanks" in answer):
        print(who("You're welcome!"))
    elif ("how old" in answer):
        print(who("I'm 734 years old!"))
    elif "sing" in answer:
        print(who("Which song do you want me to sing!"))
    elif "wow" in answer:
        print(who("I know right?"))
    elif "smart" in answer:
        print(who("Thank you! I bet you are even smarter"))
    elif "guess" in answer:
        print(who("What if I get it wrong?"))
    elif "what" in answer:
        print(who("I'm pretty sure you know the answer for that"))
    elif "no" in answer:
        print(who("Why not?"))
    elif "yes" in answer:
        print(who("Amazing!"))
    elif "anything" in answer:
        print(who("okay"))
    elif "friend" in answer:
        print(who("Sure!"))
    elif answer == "" or answer == " ":
        print(who("You didn't say anything my friend"))
    elif "because" in answer:
        print(who("Sorry, that can't be a reason"))
    elif "can" in answer:
        if ("'t" in answer):
            print(who("why can't you"))
        else:
            print(who("Can you?"))
    elif "okay" in answer:
        print(who("Really? You are very kind"))
    elif "why" in answer:
        print(who("Because....I don't know honestly"))
    elif "human" in answer or "machine" in answer:
        print(who("I'm actually a human, my real name is " + name))
    else:
        print(who(choice(answer_list)))
def who(content):
    return "Chatbot: " + content
def talk(name):
    while True:
        answer = input(name.capitalize() + ": ")
        answer = answer.lower()
        space()
        if answer == "stop":
            print("Chatbot: Goodbye " + name.capitalize() + "!")
            return False
        options(name, answer)
        space()
def rockpaperscissors():
    #player chooses rock, paper, scissor
    totalattempt = 5
    cscore = 0
    pscore = 0
    while totalattempt > 0:
        computerList = ["rock", "paper", "scissors"]
        computer = choice(computerList)
        computer = computer.lower()

        for idx in range(0, 2): print(" ")
        player = input("rock, paper, or scissors? ")
        player = player.lower()
        w = "You Won!"
        l = "You Lose!"
        if (player.isalpha() == False):
            print("That's not a word!")

        elif (player == "stop"):
            print("Goodbye my friend!")
            totalattempt = -10

        elif (player == "rock" or player == "paper" or player == "scissors"):
            print(" ")
            print("----------------------------------")
            print("rock paper scissors shoot!")
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
                if (computer == "scissors"): print(w); pscore += 1
                elif (computer == "paper"): print(l); cscore += 1
            elif (player == "scissors"):
                if (computer == "paper"): print(w); pscore += 1
                elif (computer == "rock"): print(l); cscore += 1
            elif (player == "paper"):
                if (computer == "scissors"): print(l); cscore += 1
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

# --- Put your main program below! ---
def main():
    space()
    name = input("Chatbot: Hello, my name is Chatbot!, what's your name? ")
    name = name.lower()
    space()
    introduction(name)
    space()
    choice = input("Chatbot: Do you want to play a game or talk with me? ")
    choice = choice.lower()
    if "game" in choice:
        space()
        print("Let's play rock paper scissors!")
        rockpaperscissors()
    elif "talk" in choice:
        space()
        print("Okay! Do you have any questions for me? ")
        space()
        talk(name)
    else:
        space()
        decide = input("Are you sure? ")
        decide = decide.lower()
        if decide == "yes":
            space()
            print("Alright, see you next time!")
        else:
            main()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
