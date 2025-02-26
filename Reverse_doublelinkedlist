#REVERSING IN DOUBLE LINKED LIST
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
            return
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def reverse(self):
        current = self.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
