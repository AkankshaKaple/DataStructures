#Write a Python program to get a string from a given string where all occurrences
# of its first char have been changed to '$', except the first char itself.
string = input("Enter a string : ")
for i in range(1,len(string)):
    if string[0] == string[i]:
        string = string[ : i] + "$" + string[i+1 : ] #Replace every occurrence of
                                                 # of first character by $
print(string)