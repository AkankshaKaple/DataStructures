#This program removes the duplicates from a list.
list = [2,2,2,3]
list1 = []
for i in list : # If list1 doesn't contain the element append it
    if i not in list1 :
        list1.append(list[i])
print(list1)