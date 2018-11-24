# 11. Program to reverse a string


input_string = input("Enter a string : ")
character_list_of_string = list(input_string)
character_list_of_string.reverse()
reverse_string = ''.join(character_list_of_string)
print(reverse_string)