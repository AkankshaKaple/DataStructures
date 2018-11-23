#7. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
	# Sample Words : red, white, black, red, green, black
	# Expected Result : black, green, red, white,red
n = 5
num = input("Enter the string : ")
x = num.split(",")
list = []
list = x.sort()
set = set(list)

print(set)

