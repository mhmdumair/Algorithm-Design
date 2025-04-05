arr = [6,3,5,7,2,4,8,11,21,3,14,9]

def bubblrSort(arr):
    n = len(arr)
    for j in range(n):

        swapped = False
        for i in range(n-j-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if not swapped:
            break

bubblrSort(arr)
print(arr)