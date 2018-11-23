# This the program for set union
# Union : To merge the two sets
# Union is represented by "|" in python
set1 = {1,2,3,4,"Akanksha", "kaple", 5,6,7,8}
set2 = {'a', 'b' , 'Siddhesh', 'kaple', 1,5,9,7}
print("union of the 2 sets = ", set1|set2) #Union of set1 and set2
list = []
for i in set1 :
    list.append(i) #Store the element from set1 to list
for j in set2 :
     list.append(j)      #STore the elments from set2 in list
set3 = set()
set3.update(list) # STore the list to set3 to remove repeated values
print(set3)