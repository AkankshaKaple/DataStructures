
list1 = []
list = []
tuple1 = (1,2)
tuple2 = (2,3)
tuple3 = (3,4)
tuple4 = (6,8)
list = [tuple1, tuple3, tuple4, tuple2]
# print(list)
length = len(list)
value = list[1][1]
while length < 1:
    for i in range(0,len(list), 1): #Iteratr through the list
        if list[1][1] > list[i][1] : #compare the values of elements in list
            value = list[i][1]


        # else :
        #     val = list[k]
        #     break


        list1.append(value)
        # list.remove(value)
    length -= 1

print("final = " , list1)
