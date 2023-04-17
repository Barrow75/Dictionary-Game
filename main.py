# Guess the word based on the definition

import random
print("Guess The Word Based On Definition!")
print("*Tip*: First letter needs to be capitalized")
print("----------------------------------------------")
print("\n")

playingAgain = "y"
while playingAgain == "y":
    word_dict = {}
    # opens and read the contents of the implemented text file
    with open("Words and Definitions.txt") as file:
        # iterates through each line and represents it as a string
        for line in file:
            # Takes current line and remove whitespaces (strip()) and split them into two parts
            word, definition = line.strip().split(': ')
            word_dict[word] = definition

    word, definition = random.choice(list(word_dict.items()))
    print("Hint: " + definition)
    word_length = len(word)
    lines = " _ " * word_length
    print(lines)

    while True:
        guess = input("Enter the word based on the definition: ")
        if guess == word:
            print(f"You guessed the correct word! The word was {word}!")
            break
        else:
            print("Try Again")
    playingAgain = input("Would you like to play again?: ")
    if playingAgain == "n":
        print("Thanks for Playing")
        break
