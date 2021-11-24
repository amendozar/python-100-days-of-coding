# Day 5 Loops

# Caclulate average height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0
for ht in student_heights:
    total_height += ht


num_std_hts = 0
for std in student_heights:
    num_std_hts += 1

print(f"total height = {total_height}")
print(f"number of students = {num_std_hts}")

avg_height = int(round(total_height / num_std_hts,0))
print(avg_height)


# Get highest score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"The highest score in the class is: {high_score}")



# Add all even numbers together between 1 to 100
total = 0
for i in range(1,101):
    if i % 2 == 0:
        total += i
print(total)



# Classic FizzBuzz problem
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
