def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits range from 0 to 9

    # Count occurrences of each digit at current place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    #  cumulative frequency
    for i in range(1, 10):
        count[i] += count[i - 1]


    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy output back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if not arr:
        return

    max_num = max(arr)
    exp = 1  # Exponent: 1, 10, 100, ...

    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Before sorting:", arr)
radix_sort(arr)
print("After sorting: ", arr)
