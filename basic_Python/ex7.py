# 7. Write a Python program to check whether a specified value is
# contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

input_list = [1,5,8,3]
number_to_check = int(input("Emter the number to check in list : "))
if number_to_check in input_list :
    print(True)
else :
    print(False)