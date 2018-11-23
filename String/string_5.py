# 5. Write a Python function that takes a list of words and returns
# the length of the longest one.
g_list_values = ["Akankaha", "AAAAKKKKCCC", "AAAAAAKDHD" , "kkkkkkkkkkkkkk"]


def list_of_word_function(l_list_values):  # Function to return the length of largest element in list
    value = len(l_list_values[0])
    for x in range(len(l_list_values)):
        if value < len(l_list_values[x]):
            value = len(l_list_values[x])
            ele = l_list_values[x]
    return value  # Resturn length of largest element


x = fun(g_list_values)  # Call the function by giving list as a parameter
print(x)