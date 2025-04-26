import math
a = [6,3,5,7,2,4,8,11,21,3,14,9]
def max_heapify(a,i,n):
    largest = i
    l = 2*i+1    # +1  because python array index starts from 0
    r = 2*i +2
    if l<n and a[l]>a[largest]:
        largest = l
    if r<n and a[r]> a[largest]:
        largest = r
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        max_heapify(a,largest,n)

def build_max_heap(a):
    n = len(a)
    for i in range(math.floor(n/2)-1,-1,-1):
        max_heapify(a,i,n)

def heapSort(a):
    build_max_heap(a)
    for i in range(len(a)-1,0,-1):
        a[0],a[i] = a[i],a[0]
        max_heapify(a,0,i-1)

print(a)
build_max_heap(a)
print(a)
heapSort(a)
print(a)



