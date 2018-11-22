#This is the  program to count the number of strings where the string length is
# 2 or more and the first and last character are same from a given list of strings.
# size = int(input("Enter size of the list : "))
# print("Enter elements in the list :")
list = ['aknaksha' , "Akanksha" , 'kaple', 'aba']
string = 0
size = len(list)
count = 0
# print(size)
for i in range(size) :
    size_ele = len(list[i]) - 1

    if len(list[i]) > 2 :

            if (list[i][0] == list[i][size_ele]): #Check if 1st and last character of
                                                # string are equal


                print(list[i])
                count+=1
print(count)


