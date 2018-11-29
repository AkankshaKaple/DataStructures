input_list = [99,11,22,3,4,5,6,7,44,66,77,88,110,8888]
list1 = [1]
hash_table = {}
for i in range(len(input_list)):
    list1.clear()
    key_v = input_list[i] % 11
    if input_list[i] not in hash_table.values():

    # print(key_v)
        for j in range(len(input_list)):
            if key_v == input_list[i]%11:
                if input_list[i] not in list1:
                    list1.append(input_list[j])
            else:
                break

    hash_table[key_v] = list1
    # print(hash_table)
    # print(list)
print(hash_table)



