arr = [42,35,12,77,54,101,5]

def bubblrSort(arr):
    n = len(arr)
    for j in range(n-1):
        swapped = False
        for i in range(n-j-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            return

bubblrSort(arr)
print(arr)