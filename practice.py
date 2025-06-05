arr = [4, 1, 2, 1, 4, 5, 8, 9, 6, 12, 14, 54, 11, 16, 13]


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break


def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp


def max_heapify(arr,i,n):
    l = 2 * i + 1
    r = 2*i +2
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r]>arr[largest]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,largest,n)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        max_heapify(arr,i,n)

def hep_Sort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        max_heapify(arr,0,i)

def mergeSort(arr):
    n = len(arr)
    mid = n//2
    l = arr[:mid]
    r = arr[mid:]

    if len(arr)<=1:
        return

    mergeSort(l)
    mergeSort(r)

    i=j=k=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            arr[k]=l[i]
            i+=1
        else:
            arr[k]= r[j]
            j+=1
        k+=1

    while i<len(l):
        arr[k] = l[i]
        k+=1
        i+=1

    while j<len(r):
        arr[k] = r[j]
        j+=1
        k+=1




print(arr)
# bubbleSort(arr)
# insertionSort(arr)
# hep_Sort(arr)
mergeSort(arr)
print(arr)
