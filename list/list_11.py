# #Write a Python program to generate all permutations of a list in Python.
#
# # # list = ['a', 'b' , 'c']
# # fact = 1
# # for i in range(1, len(list)+1) :
# #     fact = fact * i
# #
# # # print(fact)

# from itertools import permutations
# list1 = ['a', 'b', 'c']
# l = list(permutations(list1))
# print(l)
input_list = ['a', 'b', 'c', 'd']
def per(list):
    if len(list) == 0:
        return []

    if len(list) == 1:
        return [list]
    list2 = []

    for i in range(len(list)):
        temp1 = list[i]
        temp2 = list[:i] + list[i + 1:]


        for p in per(temp2):
            list2.append([temp1] + p)
    return list2


for p in per(input_list):
    print(p)
