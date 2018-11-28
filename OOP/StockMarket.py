# import re
#
# f = open("Stock.txt", "r")
# r1  = re.findall(r"^\w+",f)
# print(r1)

import re

datafile = file('Stock.txt')
found = False
for line in datafile:
    if blabla in line:
        found = True
        break