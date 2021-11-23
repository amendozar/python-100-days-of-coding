# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("You're at a cross road. Which direction you want to travel? Type 'right' or 'left'\n")

if direction.lower() == "left":
    # continue to next step - lake
    river = input("You've come to a lake. There is an island in the middle of the lake. What do you do? Type 'swim' or 'wait'\n")
    if river.lower() == "wait":
        # continue to next step - house
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if door.lower() == "yellow":
            # picked correct door
            print("You found the treasure.! You win!")
        else:
            print("Game over.")
            # picked wrong door - blue
            if door.lower() == "blue":
                print("The room was full of wild beasts and you were torn apart. Game Over")
            # picked wrong door - blue
            elif door.lower() == "red":
                print("The room was on fire and were burned to death. Game Over.")
            # typed anything else
            else:
                print("You chose a door that doesn't exist. Game over.")
    else:
        # islant step - picked swim
        print("You were attacked by trout. Game Over.")
else:
    # direction step - picked right
    print("You fell into a hole. Game Over.")







# if direction.lower() == "left":
#     river = input("You've come to a lake. There is an island in the middle of the lake. What do you do? Type 'swim' or 'wait'\n")
# else:
#     print("You fell into a hole. Game Over.")

# if river.lower() == "wait":
#     door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
# else:
#     print("You were attacked by trout. Game Over.")

# if door.lower() == "yellow":
#     print("You found the treasure.! You win!")
# elif door.lower() == "blue":
#     print("You were eaten by beasts. Game Over")
# elif door.lower() == "red":
#     print("You were burned by fire. Game Over.")
# else:
#     print("Game over.")





