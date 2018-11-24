# 6. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import *
input_date_1 = date(2014, 7, 2)
input_date_2 = date(2014, 7, 11)
difference = input_date_2 - input_date_1
print(difference)

