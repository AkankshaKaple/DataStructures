# Write a Python program to print a specified list after removing
# the 0th, 4th and 5th elements.

list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a1 = list[0]
a2 = list[4]
a3 = list[5]
list.remove(a1)
list.remove(a2)
list.remove(a3)
# del(list[5])
print(list)
