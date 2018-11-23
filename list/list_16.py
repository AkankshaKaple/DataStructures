#16. Write a Python program to split a list based on first character of word.
from itertools import *
from operator import *
list = ["Akanksha", "Kaple", "Aishwarya", "kalpande"]
list2 = []
# for i in list :
#     if list[i][1] == list[i+1][1]:
#         if i not in list2 :
#             list2.append(list[i])
#             list2.append(list[i+1])
# print(list2)

for l,w in groupby(sorted(list), key=itemgetter(0)) :
    # It print the values such that the first alphabet becomes the key
    # and by using sorted() it'll group the elements with same 1st
    # alphabet
    print(l)
    for i in w :
        print(i)