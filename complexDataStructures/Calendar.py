import calendar

month = int(input("Enter month : "))
year = int(input("Enter year : "))
print(calendar.month(year,month))


# # year = int(input("ENter year:"))
# # month = int(input("Enter month : "))
#
# #
# # year1 = year - ((14 - month)/12)
# # x = year1 + (year1/4) - (year1/100) + (year1/400)
# # month1 = month + 12*((14-month)/12) - 2
# def leapYear(self, year):
#     if len(year) == 4:
#         if int(year) % 400 == 0:
#             if int(year) % 100 == 0:
#                 if int(year) % 4 == 0:
#                     return True
#                 else:
#                     return False
#             else:
#                 return True
#
#         else:
#             return False
#     else:
#         return True
#
#     return
#

# week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']


# if month == 'January' or 'March' or 'May' or 'July' or 'August' or 'October' or 'December':
#     number_of_days = 31
# elif month == "April" or 'June' or 'September' or 'November' :
#     number_of_days = 30
# elif month == 'February':
#     if leapYear(year) == True:
#         number_of_days = 29
#     else:
#         number_of_days = 28
#
# calender = [month,range(1,number_of_days+1)]
#
# for month, days in calender:
#         # Print month title
#         print('{0} {1}'.format(month, year).center(20, ' '))
#         # Print Day headings
#         print(''.join(['{0:<3}'.format(w) for w in week]))
#         # Add spacing for non-zero starting position
#         print('{0:<3}'.format('')*start_pos, end='')
#
#         for day in days:
#             # Print day
#             print('{0:<3}'.format(day), end='')
#             start_pos += 1
#             if start_pos == 7:
#                 # If start_pos == 7 (Sunday) start new line
#                 print()
#                 start_pos = 0 # Reset counter
#         print('\n')

