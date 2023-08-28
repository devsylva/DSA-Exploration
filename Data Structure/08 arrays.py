# Creating an array of integers
my_array = [10, 20, 30, 40, 50]

# Accessing elements by index
print("Element at index 0:", my_array[0])  # Output: Element at index 0: 10
print("Element at index 2:", my_array[2])  # Output: Element at index 2: 30

# Modifying an element
my_array[3] = 45
print("Modified array:", my_array)  # Output: Modified array: [10, 20, 30, 45, 50]

# Length of the array
length = len(my_array)
print("Array length:", length)  # Output: Array length: 5

# Adding an element at the end
my_array.append(60)
print("Array after append:", my_array)  # Output: Array after append: [10, 20, 30, 45, 50, 60]

# Removing an element by value
my_array.remove(30)
print("Array after remove:", my_array)  # Output: Array after remove: [10, 20, 45, 50, 60]

# Finding index of an element
index = my_array.index(45)
print("Index of 45:", index)  # Output: Index of 45: 2

# Checking if an element exists in the array
exists = 50 in my_array
print("Does 50 exist?", exists)  # Output: Does 50 exist? True
