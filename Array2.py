# This program gets the number of occurrences of a specified element in
# an array.
from array import *
count = 0 # It counts the number of occurrences of the number
UserArray = array('i' , [])
size = int(input("Enter size of array : "))
print("Enter elements in array : ")
for i in range(size) :
    item = int(input())
    UserArray.append(item)
element =int(input("Enter the element you want to see the occurance for : "))
for i in range(size) :
    if element == UserArray[i]:
        count += 1 #It counts the number of occurrences of the number
print("Number of occurance of " + str(element) + " in array is : " + str(count))

