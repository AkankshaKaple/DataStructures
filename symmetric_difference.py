# This the program for symmetric difference
# Setsymmetric difference : To get the elemnts present in
# set1 but not in set2 and set2 but not in set1
# symmetric difference is represented by "^" in python
set1 = {1,2,3,4,"Akanksha", "kaple", 5,6,7,8}
set2 = {'a', 'b' , 'Siddhesh', 'kaple', 1,5,9,7}
print("set1^set2  : ", set1^set2)
#Elements present in set1 but not in set2 and set2 but not in set1
list =[]
set3 = set()
set4 = set()
# (A^B) = (A-B)&(B-A)

####### A-B #######
for i in set1 :      # Taking element in set1 but not in set2
    if i not in set2 :
        list.append(i)

####### B-A ########
for j in set2 :      # Taking elements in set2 but not in set1
    if j not in set1 :
        list.append(j)

set3.update(list)
set4.update(list)

########## (A-B)&(B-A) ############
for i in set3 :   # Merging set1 and set2
    list.append(i) #Store the element from set3 to list
for j in set4 :
     list.append(j)      #STore the elments from set4 in list

set5 = set()
set5.update(list) # STore the list to set5 to remove repeated values
print(set5)
print("set1 - set2 : " , i)



