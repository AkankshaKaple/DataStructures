class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None



    # def insertion(self, data):
    #     # new_node = Node(data)
    #     # new_node.next = previous_node.next
    #     # previous_node.next = new_node
    #
    #     length = ll.traverse()
    #
    #     new_node = Node(data)
    #     if self.head is None:
    #         self.head = new_node
    #     else:
    #         last_node = self.head
    #         while last_node.next != None:
    #             last_node = last_node.next
    #         last_node.next = new_node
    #
            # for i in range(length):
            #     if last_node.data > last_node.next.data:
            #         temp_node = last_node
            #         last_node = last_node.next
            #         last_node.next = temp_node
            # return
    #
    #
    #
    #     # current_node = self.head
    #     # for i in range(length):
    #     #     if current_node.data > current_node.next.data:
    #             temp_node = current_node
    #             current_node = current_node.next
    #             current_node.next = temp_node
    #     #     return
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            pointer = self.head
            if self.head.data > data:
                self.head = new_node
                new_node.next = pointer

            if self.head.data < data:
                temp_node = self.head
                while temp_node.next != None:
                    if pointer.data < new_node.data:
                        temp_node = pointer
                    pointer = pointer.next

                if pointer.data < data:
                    temp_node = pointer

                temp_node1 = temp_node.next
                temp_node.next = new_node
                new_node.data = temp_node1

        return


    def print(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next

    def traverse(self):
        count = 0
        current_node = self.head
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        # print(count)
        return count


ll = LinkedList()
ll.append(12)
ll.append(4)
ll.append(17)
ll.print()
t = ll.traverse()
print("trav ", t)


        # if new_node.data > previous_node.data:
        #     new_node.next = previous_node.next
        #     previous_node.next = new_node
