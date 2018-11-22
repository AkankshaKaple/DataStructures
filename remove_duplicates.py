list = [2,2,2,3]
list1 = []
value = list[0]
for i in range(1,len(list)) :
    if value == list[i] :
        value = list[i]
        list.remove(list[i])
print(list)