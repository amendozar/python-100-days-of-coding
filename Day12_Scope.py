################### Scope ####################

""" enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}") """

# Local Scope
# exist within functions

""" def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion() """
# can't pring 'potion_strenght' variable because local scope

# Global Scope
# difference is where the function / object is defined
# player_health = 10 # global scope, available anywhere else in code; not in a function


# Block Scope? Nope
""" game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy) """


