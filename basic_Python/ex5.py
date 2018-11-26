# 5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.
import calendar

month = int(input("Enter month : "))
year = int(input("Enter year : "))
print(calendar.month(year,month))


