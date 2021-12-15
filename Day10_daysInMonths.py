def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# my solution
# def days_in_month(year_input, month_input):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year_input) == False and (month_input == 2):
      return 28
  if is_leap(year_input) == False and (month_input == 9 or month_input == 11):
      return 30
  if is_leap(year_input) == False and (month_input == 10 or month_input == 12):
      return 31
  if is_leap(year_input) == False and (month_input % 2 != 0 or month_input == 8):
      return 31
  if is_leap(year_input) == False and (month_input % 2 == 0 or month_input != 8 or month_input == 9):
      return 30
  if is_leap(year_input) == True and (month_input ==2 ):
      return 29

# instructor solution 
def days_in_month(year, month):
    """Take a year and month and return the number of days. 
    This take into account leap years"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)