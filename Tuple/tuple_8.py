#8. Write a Python program to remove an item from a tuple.
tuple = 1,2,3,4,5,"Akanksha", "Kaple"
location = int(input("Enter the location of item ypu want to remove : "))
tuple = tuple[:location] + tuple[location+1:]
print(tuple)