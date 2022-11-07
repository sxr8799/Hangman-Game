import random
from hangman_words import word_list
from hangman_art import stages, logo
import os

# Importing the stages from hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1
end_of_game = False

print(logo)

# Creating the blanks

display = []
guess_list = []
for _ in range(word_length):
    display += "_"

print(f"You need to guess {len(display)} letters to clear the game.\n\n{' '.join(display)}\n")
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('clear')
# Checking the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess not in guess_list:
      guess_list.append(guess)
    elif guess in guess_list:
      print(f"You have already guessed {guess}\nHere is a list of all the letters that have been guessed {guess_list}")

# Checking if the user is wrong.
    if guess not in chosen_word:
# If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life\nHere is a list of all the letters that have been guessed {guess_list}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word chosen was {chosen_word}")

# Joining all the elements in the list and turning it into a String.
    print(f"{' '.join(display)}")

# Checking if the user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

# Importing the stages from hangman_art.py
    print(stages[lives])
