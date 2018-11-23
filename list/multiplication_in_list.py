#Program to find multiplication of all the elments in the list
size = int(input("Enter size of the list : "))
print("ENter elements in lsit :")
list = []
for i in range(size) :
    list.append(int(input())) #Take user input and add it in the list
# print(list)
mul = 1
for i in range(len(list)) : # Iterate to get every element
                            #  in list
    mul = mul * list[i]     # multiply every element with mul
print("Addition of elements in list = ", mul)