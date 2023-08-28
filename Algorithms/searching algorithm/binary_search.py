def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# Example sorted array
sorted_array = [1, 2, 3, 5, 7, 9, 11, 13]

# Target value to search for
target_value = 7

# Perform binary search
result_index = binary_search(sorted_array, target_value)

if result_index != -1:
    print(f"Target value {target_value} found at index {result_index}.")
else:
    print("Target value not found.")
