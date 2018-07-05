while True:
    word = input("Type a word for someone to guess: ")

    # Converts the word to lowercase
    word = word.lower()

    # Checks if only letters are present
    if(word.isalpha() == False):
        print("That's not a word!")

    else:
        break

# Some useful variables
guesses = []
maxfails = 7
fails = 0
wordSpace = []

for letters in word:
    wordSpace.append("__")

for idx in range(0, 20):
    print(" ")

done = False

while not done:
    print("---------------------------------------------------")
    print("Lives left: ", maxfails - fails)
    print("Guesses so far: ", guesses)
    print("Current word: ", wordSpace)

    guess = input("Guess a letter: ")
    guess.lower()

    if (len(guess) > 1):
        print("That's too long")
    elif (guess.isalpha() == False):
        print("Only type a letter")
    elif (guess in guesses):
        print("You already guessed that!")
    else:
        guesses.append(guess)

        if (guess in word):
            print("You got a letter!")
            for i in range(0, len(word)):
                if word[i] == guess:
                    wordSpace[i] = guess
                done = True;
            for i in range(0, len(wordSpace)):
                if (wordSpace[i] == "__"):
                    done = False;
                    break
            if done:
                print("You Won!")
        else:
            print("Wrong Guess!")
            fails += 1

            if (fails >= maxfails):
                print("You're done!")
                done = True
        
        
