def quickSort(array, p, r):
    if p < r:
        # Partition the array and get the pivot index
        q = partition(array, p, r)
        # Recursively sort elements before and after partition
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)

def partition(array, p, r):
    # Choose the rightmost element as pivot
    pivot = array[r]
    i = p - 1  # Pointer for the greater element

    # Traverse through all elements
    for j in range(p, r):
        if array[j] <= pivot:
            # If current element is smaller than pivot
            i = i + 1
            array[i], array[j] = array[j], array[i]  # Swap

    # Swap the pivot element with the greater element at i+1
    array[i + 1], array[r] = array[r], array[i + 1]

    # Return the pivot index
    return i + 1

# Example usage:
arr = [6, 3, 5, 7, 2, 4, 8, 11, 21, 3, 14, 9]
print("Before sorting:", arr)
quickSort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
