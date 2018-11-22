# Tis program shows the iteration in set
set1 = set()
list = []
size = int(input("Enter the size of set : "))
print("Enter elements : ")
for i in range(size):
    value = input()
    list.append(value)  # Add value onto the list
    # print(value)
    set1.update(list)  # Add list onto the set
    # print(set1)
print(set1)

for i in set1 : #Iteration on set to print the values in set
    print(i)



# Always save values given by user for set in a list....otherwise set will
# treat a string as a set....e.g., val = Akanksha --> {'A','a','k','s','n','h;}
# Update accepts list as parameter.