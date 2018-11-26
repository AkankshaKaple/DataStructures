#This is the program to find the smallest element in the list

list = [11,13,4,15,6,27,28,1]
j = len(list)
min_val = list[0]

for i in range(0,len(list)):
    if min_val > list[i]:
        min_val = list[i]
print(min_val)
