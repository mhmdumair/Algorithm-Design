a = [6,3,5,7,2,4,8,11,21,3,14,9]

def selectionSort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if a[j]<a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx] ,a[i]

selectionSort(a)
print(a)
