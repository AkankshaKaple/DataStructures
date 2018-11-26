# 26. Write a Python program to count the number occurrence of a
# specific character in a string.

user_string = input("Enter a string : ")
user_char = input("Enter a character in the string : ")
print("Occurrence of '",user_char, "' in '",user_string, "' is : ", user_string.count(user_char))