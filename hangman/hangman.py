import os
import random

print("-- hangman startup --")

#staging word
word = "octopus"

#setup
incorrect_guess_count = 0
guessed_word = ""
correctly_guessed_letters = ""
incorrectly_guessed_letters = ""

WORD_LIST = os.path.join("hangman/Scrabble-master/scrabble/sowpods.txt")
wordlist = open(WORD_LIST).readlines()
# Get rid of newlines
wordlist = [word.lower().strip() for word in wordlist]

hangman_ascii = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# FUNCTIONS

# startup game w/ instructions
def printIntro():
    print("\nThis is a game of hangman. Guess which letters are used to makeup hidden word. Make six wrong guesses and the game is over")


# get a new word
def getNewWord():
    global word
    global guessed_word
    word = random.choice(wordlist)
    
    for c in word:
        guessed_word = guessed_word + "_"

    # print("DEBUG The new word is " + word)


# feedback after a guess
def displayGameState():
    # print the hangman
    print(hangman_ascii[incorrect_guess_count])

    # if we've gone over the allowable guesses do not print game state
    if incorrect_guess_count < 6:
        print("\nWORD: ", end = '')
        for g in guessed_word:
            print(g + " ", end = '')

        print("")
        print("Correctly guessed letters: " + correctly_guessed_letters)
        print("Incorrectly guessed letters: " + incorrectly_guessed_letters)
        # print("DEBUG incorrect guesses: " + str(incorrect_guess_count) + "\n")


# check an inputted guess
def checkGuess(guess):
    global correctly_guessed_letters
    global guessed_word
    global incorrectly_guessed_letters
    global incorrect_guess_count
    
    if guess in word:
        # print("A CORRECT LETTER HAS BEEN FOUND")
        positions = [pos for pos, char in enumerate(word) if char == guess]
        # print(positions)
        correctly_guessed_letters += guess + " "
        
        strlist = list(guessed_word)
        for p in positions:
            strlist[p] = guess
            
        guessed_word = ''.join(strlist)
    else:
        incorrect_guess_count += 1
        incorrectly_guessed_letters = incorrectly_guessed_letters + " " + guess

def mainLoop():
    global incorrect_guess_count
    
    # keep guessing until maxGuesses
    if incorrect_guess_count < 6:
        if guessed_word != word:
            
            input_text = input ("Guess a letter: ")

            checkGuess(input_text)
            displayGameState()

            mainLoop()
        else:
            print("\nYOU WON! Feast on the bones of your enemy. \n")
    else:
        print("\nThe word was " + word + ", IDOIT! \n")



# setup
printIntro()

# set first word
getNewWord()

# display initial game state
displayGameState()

# main loop
mainLoop()















