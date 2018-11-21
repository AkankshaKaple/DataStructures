string = input("Enter the string : ")

dict = {}
for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count+=1
        key = string[i]
        value = count
        dict[key] = value
        dict.update(dict)
print(dict)

