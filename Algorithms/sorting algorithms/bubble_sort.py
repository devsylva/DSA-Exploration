def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example array
my_array = [64, 34, 25, 12, 22, 11, 90]

# Perform bubble sort
bubble_sort(my_array)

print("Sorted array:", my_array)
