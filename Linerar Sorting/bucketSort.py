arr = [0.1, 0.4, 0.84, 0.12, 0.78, 0.96, 0.44, 0.35]

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucketSort(array):
    bucket = [[] for _ in range(10)]  # 10 buckets

    # Put elements into buckets
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort each bucket using insertion sort
    for b in bucket:
        insertion_sort(b)

    # Concatenate all buckets
    k = 0
    for b in bucket:
        for val in b:
            array[k] = val
            k += 1

    return array

print(arr)
bucketSort(arr)
print(arr)
