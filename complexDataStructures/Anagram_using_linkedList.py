# Anagram using Linked List

class Node:
    # It creates a node with data and next field
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# It addes the data to the end of list
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next
            last_node.next = new_node
        return


    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

# It adds data at perticular position
    def insertion(self,previous_node, data):
        new_node = Node(data)
        # Create new node with given data in it
        new_node.next = previous_node.next
        # Save address of next node into new node
        previous_node.next = new_node
        # Then set adress of new node into the previous node


# It deletes the node at the end of list
    def deletion(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            current_node = None
        return

        previous_node = None
        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node = None
        return

# It calculates the number of nodes in the linked list
    def traverse(self):
        count = 0
        current_node = self.head
        while  current_node.next != None:
            count += 1
            current_node = current_node.next
        # print(count)
        return count

# It reverses the list
    def reverse(self):
        while ll.traverse() > 0:
            current_node = self.head
            if current_node.next == None:
                print(current_node.data)
                self.head = current_node.next
                current_node = None
            return

        previous_node = None
        while current_node.next != None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = current_node.next
        current_node = None
        return


ll = LinkedList()
# ll.append(12)
# ll.append(1)
# ll.append('ABC')
# ll.append("XYZ")
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
                ll.append(number)

ll.print()
length = ll.traverse()
for iterating_number in range(length):
    for iterating_number1 in range(length):
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
