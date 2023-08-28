class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from empty queue")

    def size(self):
        return len(self.items)

# Creating a queue
my_queue = Queue()

# Enqueueing elements into the queue
my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)

# Peeking at the front element
print("Front element:", my_queue.peek())  # Output: Front element: 5

# Dequeueing elements from the queue
print("Dequeued:", my_queue.dequeue())  # Output: Dequeued: 5
print("Dequeued:", my_queue.dequeue())  # Output: Dequeued: 10

# Checking if the queue is empty
print("Is queue empty?", my_queue.is_empty())  # Output: Is queue empty? False

# Getting the size of the queue
print("Queue size:", my_queue.size())  # Output: Queue size: 1
