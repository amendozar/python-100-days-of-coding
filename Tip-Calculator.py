# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


tip_percent = tip / 100
print(tip_percent)
total_tip = bill * tip_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people

final_bill = round(bill_per_person, 2)

print("Each person should pay: $" + str(final_bill))


