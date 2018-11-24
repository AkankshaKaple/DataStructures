#  Write a Python program to get a list, sorted in increasing
# order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


sorted_list = []
list_of_tuples = []
tuple1 = (1,2)
tuple2 = (2,3)
tuple3 = (3,4)
tuple4 = (6,8)
list_of_tuples = [tuple1, tuple3, tuple2, tuple4]
print(list_of_tuples)
length = len(list_of_tuples)
lowest_value = list_of_tuples[1][1]

for i in range(len(list_of_tuples)):
    for j in range(1, len(list_of_tuples)):
        if i != j:
            if list_of_tuples[i][1] > list_of_tuples[j][1]:
                lowest_value = list_of_tuples[j]
            else:
                lowest_value = list_of_tuples[i]
        if lowest_value not in sorted_list:
            sorted_list.append(lowest_value)
        if i == len(list_of_tuples):
            sorted_list.append(list_of_tuples[i])
print(sorted_list)

# print(" ", sorted(list, key=last))