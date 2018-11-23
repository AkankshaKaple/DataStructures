#15. Write a Python program to find common items from two lists.
list1 = [0,11,33,345,555,66]
list2 = [33,44,55,66,88]
lis = [(x) for x in list1 for y in list2 if x == y]
#Check if there is any value which is common in both lists
print("Common elements are :", lis)

