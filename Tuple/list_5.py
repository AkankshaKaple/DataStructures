#5. Write a Python program to find the repeated items of a tuple.
tuple = 1,2,3,1,2,3,4,5
list = []
# for i in list:
#     if i not in list :
#         list.append(tuple(i))    ##NOT WORKING
# print(list)
for i in range(len(tuple)) :
    count = tuple.count(tuple[i])
    if count > 1 :
        # print(tuple[i])
        if i not in list :
            list.append(tuple[i])
print(list)