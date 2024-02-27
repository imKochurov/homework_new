class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def delete(self, data):
        if self is None:
            return self
        # Пошук елемента, який потрібно видалити
        if data < self.data:
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            # Випадок 1: Вузол має нуль або один дочірній вузол
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            # Випадок 2: Вузол має два дочірніх вузла
            # Замінюємо поточний вузол найменшим вузлом в правому піддереві (або найбільшим в лівому піддереві)
            temp = self.right.min_value_node()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self


    def min_value_node(self):
        current = self
        while current.left is not None:
            current = current.left
        return current


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()



if __name__ == '__main__':

    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.PrintTree()
    print('\n')
    root.delete(6)
    root.PrintTree()
