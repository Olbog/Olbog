class Node:

    def __init__(self, value):
        self.right = None
        self.left = None
        self.root = value
    

    def Insert(self, value):

        if self.root:
            if value < self.root:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.Insert(value)
            elif value > self.root:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.Insert(value)
            
        else:
            self.root = value



    def Print_tree(self):
        if self.left:
            self.left.Print_tree()
        print(self.root)
        if self.right:
            self.right.Print_tree()


    def Traversal (self, root):
        result = []
        if root:
            result = self.Traversal(root.left)
            result.append(root.value)



node = Node(10)
node.Insert(2)
node.Insert(6)
node.Insert(3)
node.Insert(46)
node.Insert(9)
node.Insert(11)
node.Insert(16)
node.Insert(7)
node.Insert(14)

node.Print_tree()