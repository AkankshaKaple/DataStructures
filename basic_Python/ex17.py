# 17. Write a program to get execution time for a Python method.

from time import *
start_time = time()
print(start_time)


def addition(number1, number2):
    result = number1 + number2
    return result


user_number1 = int(input("Enter an integer : "))
user_number2 = int(input("Enter an integer : "))
result_from_method = addition(user_number1,user_number2)
print(result_from_method)
stop_time = time()
print(stop_time)
total_time = stop_time - start_time
print(total_time , "miliseconds")