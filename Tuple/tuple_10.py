#10. Write a Python program to reverse a tuple.

tuple = 1,2,3,4,"Akanksha"
list = []
length = len(tuple)-1
while length >= 0 :
    temp = tuple[length]
    list.append(temp)
    length-=1
print(list)

# a = [tuple[l] for l in range(0,len(tuple),-1) ]
# print(a)
# a = [While len > -1 ]