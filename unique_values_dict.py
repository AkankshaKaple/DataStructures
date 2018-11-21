size = int(input("Enter the size of dictionary : "))
dict = {}
set1 = set()
for i in range(size) :
    input_key = input("Give key to add onto the dictionary : ")
    input_value = input("Give value to add onto the dictionary : ")
    dict[input_key] = input_value
    dict.update(dict)

set1 = set(dict.values()) # copy the value part into a set
print(set1)