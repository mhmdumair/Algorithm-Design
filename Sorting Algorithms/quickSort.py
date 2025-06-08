def quickSort(array, start, end):
    if start < end:
        # Partition the array and get the pivot index
        pivotIndex = partition(array, start, end)
        # Recursively sort elements before and after partition
        quickSort(array, start, pivotIndex - 1)
        quickSort(array, pivotIndex + 1, end)

def partition(array, start, end):
    pivot = array[end]  # Choose the rightmost element as pivot
    smallerElementIndex = start - 1  # Pointer for the smaller element

    for currentIndex in range(start, end):
        if array[currentIndex] <= pivot:
            # Swap elements
            smallerElementIndex += 1
            array[smallerElementIndex], array[currentIndex] = array[currentIndex], array[smallerElementIndex]

    # Swap pivot into its correct position
    array[smallerElementIndex + 1], array[end] = array[end], array[smallerElementIndex + 1]
    return smallerElementIndex + 1

# Example usage
arr = [6, 3, 5, 7, 2, 4, 8, 11, 21, 3, 14, 9]
print("Before sorting:", arr)
quickSort(arr, 0, len(arr) - 1)
print("After sorting:", arr)
