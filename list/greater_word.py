# This program finds the list of words that are longer than n
# from a given list of words
list = ["Akanksha","Rajendra", "Kaple", "Siddhesh"]
word = len(list[0])
number = int(input("Enter number : ")) # Take the number from user
for i in range(len(list)) :
    if len(list[i]) > number :
        print(list[i])


