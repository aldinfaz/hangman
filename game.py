#imports
import random

#all possible words
word_list = ["apple", "pear", "bear", "orange", "airplane", "walter", "white"]

#calculates how many letters to display to the user
def display_calc(word, guessed):
    display = ""
    for char in word:
        if char in guessed:
            display += char + " "
        else:
            display += "_ "

    return display.strip() 

def hangman():
    #initliazing basic variables
    mistakes = 6
    guessed = []
    correct = 0
    

    #selects random word/answer 
    word = random.choice(word_list)

    #displayed word
    display = display_calc(word, guessed)
    
    #loop that pretty much runs the game
    while mistakes > 0:
        print(f'Word: {display}')
        print(f'Mistakes left: {mistakes}')
        guess = (input("Enter a letter: ")).lower()

        if not guess.isalpha():
            print("Must be a LETTER. Try again.")
        
        else:

            if guess not in guessed:
                guessed.append(guess)

                if guess in word:
                    print("Correct!")
                    display = display_calc(word, guessed)
                    if "_" not in display:
                        break

                elif guess not in word:
                    print("Incorrect.")
                    mistakes -= 1

            elif guess in guessed:
                print("Already guessed. Try again.")
        
        print()
    

    #after game is done
    if "_" not in display:
        print("You win! Congrats!")
    
    else:
        print("You lost...")
        
hangman()