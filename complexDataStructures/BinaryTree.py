

class Node:
    def __init__(self,left,right,value=None):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self,root):
        self.root = None

    def insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,current_node):
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else:
                self._insert(value,current_node.left)

        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._insert(value,current_node.right)

    def printing(self):
        if self.root != None:
            self._printing(self.root)

    def _printing(self,current_node):
        if current_node != None:
            self.printing(current_node.left)
            print(current_node.value)
            self.printing(current_node.right)

    # def fill_tree(tree,num_ele = 100,max_int = 1000):


list = [6,5,9,3,4]
tree = BST(list)
for i in range(len(list)):
    tree.insert(list[i])
