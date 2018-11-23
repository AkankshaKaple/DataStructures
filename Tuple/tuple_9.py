#9. Write a Python program to slice a tuple.
tuple = 1,2,3,4,5,"Akanksha", "Kaple"
start = int(input("Enter the starting position : "))
end = int(input("Enter the ending position : "))
tuple = tuple[start-1:end+1]
print(tuple)