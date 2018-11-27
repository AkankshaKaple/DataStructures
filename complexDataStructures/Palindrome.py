# 5 This program checks if the given string is palindrom or not

user_string = list(input("Enter a string: "))
original_queue = list(user_string)
check_queue = []
for iterating_number in range(len(user_string)):
    value = user_string.pop()
    check_queue.append(value)

print("1--", original_queue)
print("2--", check_queue)
if check_queue == original_queue:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

