#This program deletes the first  occurrence of a perticular
# element in an array
from array import  *
UserArray = array('i' , [])  #Array given by user
size = int(input("Enter size of array : "))
print("Enter elements in array : ")
for i in range(size) :
    item = int(input())
    UserArray.append(item)
element =int(input("Enter the element whose first  occurrence you want remove : "))
for i in range(size) :
    if element == UserArray[i] :
        UserArray.remove(UserArray[i]) #Remove the first occurrence of an element
        break  # Break to avoid deleting other occurrences
    elif element != UserArray[i] :
        print("Element is not present in array")
print(UserArray)