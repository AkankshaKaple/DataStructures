# 20. Write a Python program to sort three integers without using conditional
# statements and loops

print("Enter any 3 integers : ")
list_of_integers = []
for iterating_number in range(3):  # Save the integers in a list
    list_of_integers.append(int(input()))
print("Unsorted integers : ", list_of_integers)
list_of_integers.sort()  # Sort the list
print("Sorted integers : ",list_of_integers )