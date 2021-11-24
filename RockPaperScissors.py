# Rock, Paper, Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as rd
import warnings
rps = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer_choice = rd.randint(0,2)

# print(user_choice)
# print(computer_choice)
# print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice])


# user_choice = 1
# computer_choice = 2

# My solution - specific to this lesson
# account for user input thats not 0-3
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number! You lose.")
# all possible situations for User to win
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1): 
    print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Win")
# draw
elif (user_choice == computer_choice):
    print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nIt's a draw")
# otherwise User loses
else:
    print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Lose")



# solution from instructor
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number! You lose.")
# elif (user_choice == 0 and computer_choice == 2): 
#     print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Win")
# elif (user_choice == 1 and computer_choice == 0): 
#     print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Win")
# elif (user_choice == 2 and computer_choice == 1): 
#     print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Win")
# elif (user_choice == computer_choice):
#     print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nIt's a draw")
# else:
#     print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Lose")


# user_choice = 23434
# computer_choice = 2
# Solution from comments - more scaleable
# if user_choice > 2 or user_choice < 0:
#   print("You typed an invalid number! You lose.")
 
# # this discribes all situations when computer is winning
# elif computer_choice == user_choice + 1 or computer_choice + 2 == user_choice:
#   print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Lose")

# # this discibes the equals
# elif computer_choice == user_choice:
#   print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nIt's a draw")
 
# # the rest is me winning
# else:
#   print(rps[user_choice] + "\nComputer chose:\n" + rps[computer_choice] + "\nYou Win")