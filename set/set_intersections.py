#This the program for set intersection
#Intersection : To get the common elements among the two sets
#Intersection is represented by "&" in python
set1 = {1,2,3,4,"Akanksha", "kaple", 5,6,7,8}
set2 = {'a', 'b' , 'Siddhesh', 'kaple', 1,5,9,7}
print("Intersection of set1 and set2 is -- " + str(set1 & set2))
# Intersection of set1 and set2
for i in set1 :
    for j in set2 :
        if i == j : #If element in set1 is same
                    # as element in set2 then print
            print(i)
#             set3 = set(i)
# print(set3)
