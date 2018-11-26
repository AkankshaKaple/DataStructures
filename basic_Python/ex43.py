# 43. Write a Python function to find the maximum and minimum numbers from a sequence
#  of numbers.
# Note: Do not use built-in functions.


sequence_of_numbers = [3, 4, 2, 5, 6]
storing_element = sequence_of_numbers[0]

for iterating_number in range(len(sequence_of_numbers)):
    if storing_element > sequence_of_numbers[iterating_number]:
        storing_element = sequence_of_numbers[iterating_number]
print("Minimum = ", storing_element)

for iterating_number in range(len(sequence_of_numbers)):
    if storing_element < sequence_of_numbers[iterating_number]:
        storing_element = sequence_of_numbers[iterating_number]
print("Maximum = ", storing_element)