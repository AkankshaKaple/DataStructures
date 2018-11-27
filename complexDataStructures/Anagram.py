# 14 Add the Prime Numbers that are Anagram in the Range of 0 - 1000
# in a Queue using the Linked List and Print the Anagrams from the Queue.
#  Note no Collection Library can be used.

prime_numbers = []
anagram = []
flag = 0
for number in range(0, 100):
    if number > 1:
        for iterating_number in range(2, number):
            if number % iterating_number == 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:

            if number not in prime_numbers:
                prime_numbers.append(str(number))

for iterating_number in range(len(prime_numbers)):
    for iterating_number1 in range(len(prime_numbers)):
        if len(prime_numbers[iterating_number]) == len(prime_numbers[iterating_number1]):
            if len(prime_numbers[iterating_number]) > 1:
                if len(prime_numbers[iterating_number1]) > 1:
                    queue_1 = (list(prime_numbers[iterating_number]))
                    queue_2 = (list(prime_numbers[iterating_number1]))
                    queue_1.sort()
                    queue_2.sort()
                    # print(list_1)
                    if queue_1 == queue_2:
                        print(prime_numbers[iterating_number], " is anangram of ", prime_numbers[iterating_number1])
            else:
                pass
        else:
            pass
