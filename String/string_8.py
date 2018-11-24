# 8. Write a Python program to get the last part of a string
# before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python


input_string = input("Enter a string : ")
input_character = input("Enter a character : ")
character_position = input_string.find(input_character)
print(input_string[:character_position])