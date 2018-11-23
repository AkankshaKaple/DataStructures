#This program creates the directory upto N in the form (x,x*x)

size = int(input("Enter the size of directory : "))
dict = {}
for x in range(1,size+1):
    key = x
    value = x*x
    dict[key] = value
    dict.update(dict)
print(dict)
