# 35. Write a Python program to get numbers divisible by
# fifteen from a list using an anonymous function.

list_of_integers = [21,15,30,22,44,54,45]
values_divisible_by_fifteen = list(filter(lambda iterating_number : iterating_number%15 == 0,
                                          list_of_integers))
print(values_divisible_by_fifteen)