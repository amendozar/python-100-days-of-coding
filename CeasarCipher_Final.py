# Casesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesar_logo import logo

def ceasar(start_text, shift_amount, direction_input):
    end_text = ""
    if direction_input == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direction_input}d result: {end_text}")

    # # My code - longer
    # start_text = ""
    # # encode text
    # if direction_input == "encode":
    #     for char in start_text:
    #       if char in alphabet:
    #         position = alphabet.index(char)
    #         new_position = position + shift_amount
    #         start_text += alphabet[new_position]
    #       else:
    #         end_text += char
    #     print(f"The encoded text is {start_text}")
    # # decode text
    # elif direction_input == "decode":
    #     for char in start_text:
    #         if char in alphabet:
    #             position = alphabet.index(char)
    #             new_position = position - shift_amount
    #             start_text += alphabet[new_position]
    #         else:
    #             end_text += char
    #     print(f"The decoded text is {start_text}")

print(logo)

# ask user if they want to restart
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, direction_input=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
        