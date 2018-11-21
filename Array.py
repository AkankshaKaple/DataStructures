#This program creates an array of 5 integers
# and displays the array items and accesses individual element through indices.
from  array import *
array1 = array('i' , [])
print("Enter values in an array : ")
for i in range(0,5) :
    x = int(input())
    array1.append(x)
print(array1)
index = int(input(print("Enter the index you want to access :")))
if 0 > index > 4:
    print("Enter proper value for index")
else :
    print("Element at index " + str(index) + " is : " + str(array1[index]))