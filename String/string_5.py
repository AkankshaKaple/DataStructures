#5. Write a Python function that takes a list of words and returns
# the length of the longest one.
list = ["Akankaha", "AAAAKKKKCCC", "AAAAAAKDHD" , "kkkkkkkkkkkkkk"]
def fun(list) :  #Function to return the length of largest element in list
    value = len(list[0])
    for x in range(len(list)):
        if value < len(list[x]):
            value = len(list[x])
            ele = list[x]
    return(value) #Resturn length of largest element
x = fun(list) #Call the function by giving list as a parameter
print(x)