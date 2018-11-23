#12. Write a Python program to get the difference between the two lists.
from itertools import *
list1 = [0,11,33,345,555,66]
list2 = [33,44,55,66,88,11]
list = []

l = [(list2[x] - list1[x]) for x in range(len(list2))]
print(l)

# #### If length of two lists is same ######
# if len(list1) == len(list2) :
#     for i in range(len(list1)):
#         temp = list1[i] - list2[i]
#         list.append(temp)
# elif len(list1) > len(list2):
#     for i in range(len(list2)):
#         temp = list1[i] - list2[i]
#         list.append(temp)
#
# else :
#     for i in range(len(list1)):
#         temp = list1[i] - list2[i]
#         list.append(temp)
# print(list)
#
