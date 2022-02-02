
class Node:
    def __init__(self, key=None, value=None):
        self._key = key
        self._value = value

        self.left = None
        self.right = None

        self.create_ribbing()

    def copy(self, node):
        self._key = node._key
        self._value = node._value
        self.left = node.left
        self.right = node.right

    def delete(self):
        self._key = None
        self._value = None
        self.left = None
        self.right = None

    def update(self, key, value):
        self._key = key
        self._value = value

        self.create_ribbing()

    def has_child(self):
        flag = False

        if self.right is not None or self.left is not None:
            flag = True

        return flag

    def is_empty(self):
        flag = False
        if self._key is None and self._value is None:
            flag = True

        return flag

    def create_ribbing(self):
        if not self.is_empty():
            self.left = Node()
            self.right = Node()

    def __str__(self):
        return f"Node({self._key}: {self._value})\t"

    def __repr__(self):
        if self.is_empty():
            return "Node(Empty)"
        else:
            return str(self)

class Tree:
    def __init__(self, root=Node()):
        self.root = root

    def get(self, key):
        if self.is_empty():
            print("No such key")
            return None
        else:
            if key == self.root._key:
                return self.root
            elif key > self.root._key:
                sub_tree = self.get_right_subtree()
                return sub_tree.get(key)
            elif key < self.root._key:
                sub_tree = self.get_left_subtree()
                return sub_tree.get(key)

    def insert(self, key, value):
        if self.is_empty():
            self.set_root(key, value) # добавление корневого узла
            return
        else:
            x = self.root
            if key > x._key:
                right_subtree = self.get_right_subtree()
                right_subtree.insert(key, value)
            elif key < x._key:
                left_subtree = self.get_left_subtree()
                left_subtree.insert(key, value)
            elif key == x._key:
                self.update(key, value)

    def update(self, key, new_value):
        node = self.get(key)

        if node is not None:
            node.update(key, new_value)

    def delete(self, key):
        if self.is_empty():
            return
        else:
            if key > self.root._key:
                sub_tree = self.get_right_subtree()
                return sub_tree.delete(key)
            elif key < self.root._key:
                sub_tree = self.get_left_subtree()
                return sub_tree.delete(key)
            elif key == self.root._key:

                if not self.root.has_child():
                    self.root.delete()  # оба пустые
                elif self.root.left.is_empty() or self.root.right.is_empty():
                    if not self.root.left.is_empty():
                        self.root.copy(self.root.left)
                    else:
                        self.root.copy(self.root.right)

                else:
                    right_sub_tree = self.get_right_subtree()
                    if  right_sub_tree.root.left.is_empty():
                        left_sub = self.get_left_subtree()
                        self.root.copy(self.root.right)
                        self.root.left = left_sub.root
                    else:
                        subtree = self.get_right_subtree()

                        while subtree.get_left_subtree().is_empty():
                            subtree = subtree.get_left_subtree()

                        m = subtree.root
                        _key = m._key
                        _value = m._value

                        self.delete(m._key)

                        self.root._key = _key
                        self.root._value = _value

    def is_empty(self):
        return self.root.is_empty()

    def get_right_subtree(self):
        sub_tree = Tree()
        sub_tree.root = self.root.right


        return sub_tree

    def get_left_subtree(self):
        sub_tree = Tree()
        sub_tree.root = self.root.left

        return sub_tree

    def set_root(self, key, value):
        self.root.update(key, value)

    def print_tree(self, depth=0):
        if not self.is_empty():
            print(self.root)
            # TODO: add normal print tree
            self.get_left_subtree().print_tree(depth + 1)
            self.get_right_subtree().print_tree(depth + 1)
        else:
            print("Empty")



def main():
    tree = Tree()

    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(1, "1")
    tree.insert(7, "7")

    print(tree.get(7)) #-> "7"

    tree.update(7, "77") #-> .insert(7, "77")
    print(tree.get(7)) #-> "77"

    tree.delete(5)
    print(tree.get(7))
    print(tree.get(5))


if __name__ == '__main__':
    main()
