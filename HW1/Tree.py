class Tree:

    def __init__(self, value):
        self.root = value
        self.left = None
        self.right = None
    

# обновление 
    def update(self, key, new_value):
        pass

# удаление
    def delete(self, key):
        pass

# возврат
    def get(self, key):
        pass

# добавление
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        if value < self.root:
            if self.left == None:
                self.left = Node(value)
            else:
                self.insert(value,self.left)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.inser(value, self.right)

class Node:
    
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __gt__(self,other):
        return 0
      

tree = Tree(Node(5, 25))
tree.insert(3, 9)

