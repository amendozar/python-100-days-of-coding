#Password Generator

import random as rd
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_passwords = int(input(f"How many passwords would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# select random letters
# password = ''
# for l in range(0,nr_letters):
#     password += rd.choice(letters)
# print(selected_letters)

# # select random symbols
# for sym in range(0,nr_symbols):
#     password += rd.choice(symbols)
# print(selected_symbols)

# # select random numbers
# for num in range(0,nr_numbers):
#     password += rd.choice(numbers)
# print(selected_numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
multi_passwords = []
for pws in range(0,nr_passwords):
    password = []
    for l in range(0,nr_letters):
        password.append(rd.choice(letters))
    # print(selected_letters)

    # select random symbols
    for sym in range(0,nr_symbols):
        password.append(rd.choice(symbols))
    # print(selected_symbols)

    # select random numbers
    for num in range(0,nr_numbers):
        password.append(rd.choice(numbers))
    # print(selected_numbers)

    rd.shuffle(password)
    # for loop to create string
    # final_password = ''
    # for char in password:
    #     final_password += char
    final_password = ''.join(password)
    multi_passwords.append(final_password)

print(multi_passwords)
