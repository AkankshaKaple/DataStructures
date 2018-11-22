#This is the program to find the smallest element in the list
val = 0
list = [11,2,13,4,15,6,27,28,89]
for i in range(len(list)): #Iteratr through the list

    if list[i] < list[i+1] : #compare the values of elements in list
        val = list[i]
        break
    else :
        val = list[i+1]

print(val)
    # print(i)