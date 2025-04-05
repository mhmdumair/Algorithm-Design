a = [6,3,5,7,2,4,8,11,21,3,14,9]

def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp

insertionSort(a)
print(a)