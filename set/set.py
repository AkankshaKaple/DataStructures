# This program adds the elements into a set
set1 = set()
list = []
size = input("Enter number of values you want to insert : ")
for i in range(int(size)) :
    value = (input("Enter value in set"))
    list.append(value) # Add value to the list

set1.update(list)  # Insert multiple elements into set
print(set1)
