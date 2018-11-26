# 8. Write a Python program to create a histogram from a given list of integers.


list_of_numbers = [2,5,8,4]
histogram = ''
for iterating_number in range(len(list_of_numbers)):
    histogram = ' '
    while list_of_numbers[iterating_number] > 0 :
        histogram = histogram + '@'
        list_of_numbers[iterating_number]-=1
    print(histogram)