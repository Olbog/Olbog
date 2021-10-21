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
        parent = None
        v = self.root
        while v is not None:
            parent = v
            if value < v.key:
                v = v.left
            elif value > v.key:
                v = v.right
            else:  # x == v.key
                return
        
        w = Node
    
        if parent is None:
            self.root = w
        elif value < parent.key:
            parent.left = w
        elif value > parent.key:
            parent.right = w
                

    

class Node:
    
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

    def __gt__(self,other):
        return 0
      

tree = Tree(Node(5, 25))
tree.insert(3)
print(tree)
