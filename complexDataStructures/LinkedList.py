class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


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


    def insertion(self,previous_node, data):
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node



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

    def traverse(self):
        count = 0
        current_node = self.head
        while  current_node.next != None:
            count += 1
            current_node = current_node.next
        # print(count)
        return count

#
# ll = LinkedList()
# ll.append(12)
# ll.append(1)
# ll.append('ABC')
# ll.append("XYZ")
# # ll.insertion(ll.head.next.next,16)
# t = ll.traverse()
# ll.print()
# print("Length : ", t)
