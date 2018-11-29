from DataStructures.complexDataStructures.LinkedList import *
ll = LinkedList()
node_0 = Node(0)
node_1 = Node(0)
node_2 = Node(0)
node_3 = Node(0)
node_4 = Node(0)


dictionary = {}
list = []
list1 = [99,11,22,3,4,5,6,7,44,66,77,88,110,8888]
for iterating_value in range(len(list1)):
    location = list1[iterating_value]%6
    value = list1[iterating_value]

    if location == 0:
        list = list1[iterating_value]

        # dictionary.update(list1[location],key = 0)
        # ll.print()

    if location == 1:
        list[location] = list.append(list1[iterating_value])
        # list[location] = Node(list1[iterating_value])
        dictionary.update(list1[location],key = 1)


    if location == 2:
        list[location] = list.append(list1[iterating_value])
        # list[location] = Node(list1[iterating_value])
        dictionary.update(list1[location],key = 2)


    if location == 3:
        list[location] = list.append(list1[iterating_value])
        # list[location] = Node(list1[iterating_value])
        dictionary.update(list1[location],key = 3)


    if location == 4:
        list[location] = list.append(list1[iterating_value])
        # list[location] = Node(list1[iterating_value])
        dictionary.update(list1[location],key = 4)



#     list1[location] = ll.append(list1[iterating_value])
# ll.print()
print(dictionary)

