# 2. Write a Python program which accepts a sequence of comma-separated
# numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')


user_numbers = input("Enter numbers : ")
list_of_user_defined_items = user_numbers.split(',')
print(list_of_user_defined_items)
tuple_of_user_deffined_items = tuple(list_of_user_defined_items)
print(tuple_of_user_deffined_items)