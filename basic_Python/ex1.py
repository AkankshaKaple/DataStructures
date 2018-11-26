# 1. Write a Python program which accepts the user's first
# and last name and print them in reverse order with a space between them.


user_first_name = input("Enter first name : ")
user_last_name = input("Enter last name : ")
list_of_last_name = list(user_last_name)
list_of_first_name = list(user_first_name)
list_of_first_name.reverse()
list_of_last_name.reverse()
reverse_first_name = ''.join(list_of_first_name)
reverse_last_name = ''.join(list_of_last_name)
print(reverse_first_name + " " + reverse_last_name)

