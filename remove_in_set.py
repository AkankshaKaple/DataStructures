#This is the program to remove element(s) from the set
set1 = set()
size = int(input("Enter the size of set: "))
print("Enter elements in the set : ")
list = []
for i in range(size) :
    list.append(input()) # Add value onto the list
    set1.update(list)  # Add list onto the set
print(set1)
num = int(input("How many elements you want to delete from set :"))
if num > len(set1) :
    print("Enter proper value")
else :
    for i in range(num) :
        element = input("Enter an element you want to remove : ")
        if element in set1 : # Check if the element is present in the set
            set1.remove(element) # Remove given item from the set
            print(set1)
        else :
            print("Element is not present in the set")

#.discard() : If element to be deleted is not present in the set, using .discard()
# won't generate any error message

#.remove() : If element is not present in the set, .remove() will rais an
# error message