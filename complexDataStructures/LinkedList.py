class LinkedList:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.head = None

    def linkedList(self,data):
        if self.head == None:
            self.head = data
        else:
            if