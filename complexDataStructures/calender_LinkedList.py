# import calendar
#
# month = int(input("Enter month : "))
# year = int(input("Enter year : "))
# print(calendar.month(year,month))


class Calendar:

    def leapYear(self, year):
        if len(year) == 4:
            if int(year) % 400 == 0:
                if int(year) % 100 == 0:
                    if int(year) % 4 == 0:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False
        else:
            return True

    def month_day(self,month,year):
        if month == 'January' or 'March' or 'May' or 'July' or 'August' \
                or 'October' or 'December':
            number_of_days = 31
        elif month == "April" or 'June' or 'September' or 'November' :
            number_of_days = 30
        elif month == 'February':
            if obj.leapYear(year) == True:
                number_of_days = 29
            else:
                number_of_days = 28
        return  number_of_days


    def week_day(self, month, year):

        year1 = year - ((14 - month) / 12)
        x = year1 + (year1/4) - (year1/100) + (year1/400)
        month1 = month + 12 * ((14 - month) / 12) - 2
        day1 = (1 + x + (31*month1) / 12) % 7
        return int(day1)

    def month_int(self,month):
        if month == 'January':
            return 1
        if month == 'February':
            return 2
        if month == 'March':
            return 3
        if month == 'April':
            return 4
        if month == 'May':
            return 5
        if month == 'June':
            return 6
        if month == 'July':
            return 7
        if month == 'August':
            return 8
        if month == 'September':
            return 9
        if month == 'October':
            return 10
        if month == 'November':
            return 11
        if month == 'December':
            return 12


week = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
obj = Calendar()
year = int(input("Enter year:"))
month = input("Enter month : ")
number_of_days = obj.month_day(month,year)
print(str(month) + " has " + str(number_of_days) + " number of days" + "coz year is "
      + str(year))
month_i = obj.month_int(month)
day = obj.week_day(month_i, year)
print("Day is : ", week[day])

calender_row = []
print('Mon', 'Tue', 'Wed','Thur', 'Fri','Sat','Sun')

for month_day in range(1, number_of_days):
    # for i in range(day):
        # calender_row.append(' ')
        if month_day % 7 == 0:
            calender_row.append(month_day)
        else:
            calender_row.append(month_day)

# print(calender_row)
        if len(calender_row) == 7:
            print(calender_row)
            calender_row.clear()
        else:
            print(calender_row)
            calender_row.clear()



# for month_day in range(1, number_of_days):
#     for i in range(day):
#         calender_row.append(' ')
#     if month_day % 7 == 0:
#         calender_row.append(month_day)
#     else:
#         calender_row.append(month_day)
# if len(calender_row) == 7:
#     print(calender_row)
#     calender_row.clear()









