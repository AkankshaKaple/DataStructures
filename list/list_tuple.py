
list1 = []
list = []
tuple1 = (1,2)
tuple2 = (2,3)
tuple3 = (3,4)
tuple4 = (6,8)
list = [tuple1, tuple3, tuple2, tuple4]
print(list)
length = len(list)
value = 0
# for k in range(0, len(list)) :
#     for i in range(0,len(list)): #Iteratr through the list
#         for j in range(1, len(list)):
#                 # print(list[i][1] , list[j][1])
while len(list) > 0 :
    i = 0
    j = 0
    if list[i][1] > list[j][1] : #compare the values of elements in list
        value = list[j]
        i+=1
        j+=1
        break

    else :
        value = list[i]


    if value not in list1:
        list1.append(value)
        list.remove(value)




        # list1.append(value)
        # list.remove(value)


print("final = " , list1)
