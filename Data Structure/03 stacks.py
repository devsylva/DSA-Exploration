class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Creating a stack instance
my_stack = Stack()

# Pushing elements onto the stack
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)

# Peeking at the top element
print("Top element:", my_stack.peek())  # Output: Top element: 15

# Popping elements from the stack
print("Popped:", my_stack.pop())  # Output: Popped: 15
print("Popped:", my_stack.pop())  # Output: Popped: 10

# Checking if the stack is empty
print("Is stack empty?", my_stack.is_empty())  # Output: Is stack empty? False

print("Popped:", my_stack.pop())  # Output: Popped: 5
print("Is stack empty?", my_stack.is_empty())  # Output: Is stack empty? True
