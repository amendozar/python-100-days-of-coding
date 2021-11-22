#Tip Calculator v2

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + float(tip) / 100)
# print(bill_with_tip)
# tip_percent = float(tip) / 100
# print(tip_percent)
# total_tip = bill * tip_percent
# total_bill = bill + total_tip
bill_per_person = bill_with_tip / people

final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)
print("Each person should pay: $" + str(final_bill))

