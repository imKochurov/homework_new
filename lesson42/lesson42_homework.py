class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def index(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return f"Element '{value}' not in list"
    
    def insert(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        index = 0
        while current:
            if index == position - 1:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            index += 1
        else:
            print("Помилка: Позиція перевищує розмір списку")

    def delete(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
            else:
                print("Помилка: Список порожній")
            return
        current = self.head
        index = 0
        while current:
            if index == position - 1:
                if current.next:
                    current.next = current.next.next
                else:
                    print("Помилка: Позиція перевищує розмір списку")
                break
            current = current.next
            index += 1

    def slice(self, start, end):
            if start < 0 or end < 0 or start >= end:
                print("Помилка: Неправильний діапазон")
                return None
            sliced_list = LinkedList()
            current = self.head
            index = 0
            while current and index < end:
                if start <= index < end:
                    sliced_list.append(current.data)
                current = current.next
                index += 1
            return sliced_list

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':

    my_list = LinkedList()
    my_list.append(17)
    my_list.append(4)
    my_list.append(9)
    my_list.display()

    print(my_list.index(9))

    my_list.insert(155, 2)
    my_list.display()
    my_list.slice(1, 3).display()

    my_list.delete(2)
    my_list.display()