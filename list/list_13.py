#13. Write a Python program to append a list to the second list.
list1 = [0,11,3,345,555,66]
list2 = [33,44,55,66,88]
for i in range(len(list2)) :
    list1.append(list2[i])
print(list1)

