class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Creating an instance of the linked list
my_linked_list = LinkedList()

# Appending elements to the linked list
my_linked_list.append(5)
my_linked_list.append(10)
my_linked_list.append(15)
my_linked_list.append(20)

# Displaying the linked list
my_linked_list.display()
