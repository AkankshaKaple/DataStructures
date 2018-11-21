#This program reverses order of the items in an array
from array import *
UserArray = array('i' , [])
size = int(input("Enter the size of array : "))
print("Enter : ")
for i in range(size) :
    item = int(input())
    UserArray.append(item)
print(UserArray)
# UserArray.reverse()

j = len(UserArray) - 1  #Trverse from last element to first element in an array
while j >= 0 :
    print(UserArray[j])
    j-=1