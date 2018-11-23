# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# a = {}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)
dict = {}
dict1={}
list = []
num = int(input("ENter number of divtionaries you want to concatinate:"))
while num > 0:
    size = int(input("Enter number of key value pairs you want in this dict : "))
    while size > 0:

                input_key = input("Give key to add onto the dictionary : ")
                input_value = input("Give value to add onto the dictionary : ")
                dict[input_key] = input_value
                # list.append(dict.items())  # Append key val pair from dictionay to list
                # print(dict)
                size-=1


    num-=1
# print(list)
    dict.update(dict1)
print(dict)