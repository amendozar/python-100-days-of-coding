import random as rd

logo = """
 _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______   
|       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |  
|    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||  
|   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_ 
|   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|

"""
print(logo)

# Welcome message
print("Welcome to the Number Guessing Game!")

# Randomly pick number
print("I'm thinking of a number between 1 and 100.")
number = rd.randint(1,100)

# Ask for difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
# global scope object
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

# Ask for guess from player
guess = int(input('Make a guess: '))
should_end = False
while not should_end:
    if guess > number and attempts != 0:
        print('Too high.')
        print('Guess again.')
        print(f"You have {attempts} attempts remaining to guess")
        guess = int(input('Make a guess: '))
        attempts -= 1
    elif guess < number and attempts != 0:
        print('Too low.')
        print('Guess again.')
        print(f"You have {attempts} attempts remaining to guess")
        guess = int(input('Make a guess: '))
        attempts -= 1
    elif guess == number and attempts != 0:
        should_end = True
        print(f'You got it! The answer was {number}')
    elif attempts == 0:
        should_end = True
        print("You've run out of guesses, you lose.")
# 38 lines

########## Answer ##########
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

# game()
# 49 lines