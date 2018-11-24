# 7. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
#  Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red


input_strings = input("Enter the string : ")
list_of_strings = input_strings.split(",")
list_of_strings.sort()
set_of_string = set()

for iterating_element in range(len(list_of_strings)):
    set_of_string.add(list_of_strings[iterating_element])

list_of_strings = list(set_of_string)
print(list_of_strings)




