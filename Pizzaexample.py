# Pizza example

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill += 18
        else:
            bill += 17
    else:
        if extra_cheese == "Y":
            bill += 16
        else:
            bill += 15
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill += 24
        else:
            bill += 23
    else:
        if extra_cheese == "Y":
            bill += 21
        else:
            bill +=20
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill += 29
        else:
            bill += 28
    else:
        if extra_cheese == "Y":
            bill += 26
        else:
            bill += 25
else:
    pass

print(f"Your final bill is: ${bill}.")