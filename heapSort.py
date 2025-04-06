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



