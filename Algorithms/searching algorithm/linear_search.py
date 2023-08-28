def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Target not found

# Example array
my_array = [3, 9, 7, 2, 1, 5, 8]

# Target value to search for
target_value = 5

# Perform linear search
result_index = linear_search(my_array, target_value)

if result_index != -1:
    print(f"Target value {target_value} found at index {result_index}.")
else:
    print("Target value not found.")
