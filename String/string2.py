#Write a Python program to count the number of characters (character frequency) in a string.
#	Sample String : google.com
#	Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
# from itertools import *
# from operator import *
string = input("Enter the string : ")
# for letter,count in groupby(sorted(string), key = countOf(letter,string)) :

dict = {}
for i in range(len(string)) :
    key = string.count(string[i])
    dict[string[i]] = key
print(dict)
