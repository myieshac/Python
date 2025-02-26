#INSERTION & DELETION IN DOUBLE LINKED LIST
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

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty.")
            return
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_at_location(self, location):
        if location == 0:
            self.delete_at_beginning()
            return
        current = self.head
        current_location = 0
        while current and current_location < location - 1:
            current = current.next
            current_location += 1
        if not current or not current.next:
            print("Location out of range.")
            return
        current.next = current.next.next
        if current.next:
            current.next.prev = current
        else:
            self.tail = current

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example
doubly_linked_list = DoublyLinkedList()

# Insert elements
doubly_linked_list.insert_at_end(10)
doubly_linked_list.insert_at_end(20)
doubly_linked_list.insert_at_end(30)
doubly_linked_list.insert_at_end(40)
doubly_linked_list.insert_at_end(50)

print("Initial list:")
doubly_linked_list.print_list()

print("Deleting at the beginning:")
doubly_linked_list.delete_at_beginning()
doubly_linked_list.print_list()

print("Deleting at the end:")
doubly_linked_list.delete_at_end()
doubly_linked_list.print_list()

print("Deleting at a given location:")
doubly_linked_list.delete_at_location(1)
doubly_linked_list.print_list()
