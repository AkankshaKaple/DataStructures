#Program to find sum of all the elments in the list
size = int(input("Enter size of the list : "))
print("ENter elements in lsit :")
list = []
for i in range(size) :
    list.append(int(input())) #Take user input and add it in the list
# print(list)
sum = 0
for i in range(len(list)) : # Iterate to get every element
                            #  in list
    sum = sum + list[i]     # add every element with sum
print("Addition of elements in list = ", sum)