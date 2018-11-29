# 9 Create the Week Object having a list of WeekDay objects each storing the day
# (i.e S,M,T,W,Th,..) and the Date (1,2,3..) . The WeekDay objects are stored in a
# Queue implemented using Linked List. Further maintain also a Week Object in a Queue
# to finally display the Calendar
# Note - If a particular day has no date then the date is set as empty string and
# add it to queue.

from DataStructures.complexDataStructures.LinkedList import *
from DataStructures.complexDataStructures.Calendar import *

ll = LinkedList()
calender = Calendar()
year = int(input("Enter year:"))
month = input("Enter month : ")
# number_of_days = calender.month_day(month, year)
print("Days in month are : ")
for iterating_value in range(1, calender.month_day(month,year)+1):
    ll.append(iterating_value)
ll.print()





