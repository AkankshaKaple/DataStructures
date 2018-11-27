from array import *
from collections import deque
import numpy as np
list1 = deque([])
arr = np.array([])
flag = 0

for iteration_value in range(0, 10):
    min = iteration_value * 100
    max = 100*(iteration_value + 1)
    for number in range(min,max+1):
        if number > 1:
            for iterating_number in range(2, number):
                if number % iterating_number == 0:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 1:
                if number not in list1:
                    list1.append(number)
    print("Prime number in range ",min,"-",max, "=",list1)
    row = iterating_number

    for column in range(len(list1)-1):
        column = list1.popleft()
        arr = np.append(arr, np.array([row][column]))

    # Matrix = np.array([iterating_number][list1])
    list1.clear()
print(arr)


