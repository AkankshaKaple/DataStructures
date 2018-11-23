# This the program for set difference
# Set difference : To get the elemnts present in set1 but not in set2
# Set difference is represented by "-" in python
set1 = {1,2,3,4,"Akanksha", "kaple", 5,6,7,8}
set2 = {'a', 'b' , 'Siddhesh', 'kaple', 1,5,9,7}
print("set1-set2  : ", set1-set2)
#Elements present in set1 but not in set2
print("set2-set1  : ", set2-set1)
#Elements present in set2 but not in set1
set3 = set()
lsit = []

for i in set1 :
    if i not in set2 :    # Print i if i is not present in set2
        print("set1 - set2 : " , i)
