# 17. Write a Python program to remove duplicates from a list of lists.
# 	Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# 	New List : [[10, 20], [30, 56, 25], [33], [40]]


list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list1 = []

for i in range(len(list)):
    for j in range(1,len(list)) :
        if list[i] == list[j]:
            temp = list[i]
            list.remove(temp)
            # if i not in list1 :
            #     list1.append(temp)
print(list1)