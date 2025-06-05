arr = [4,8,2,1,4,12,45,21,36,54,15,22,11,10]

def countSort(arr):
    m = max(arr)
    countArray = [0]*(m+1)
    for i in range(len(arr)):
        countArray[arr[i]]+=1
    for i in range(1,len(countArray)):
        countArray[i] = countArray[i]+countArray[i-1]

    output = [0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        index = countArray[arr[i]]
        output[index-1] = arr[i]
        countArray[arr[i]]-=1
    for i in range(len(output)):
        arr[i]=output[i]

print(arr)
countSort(arr)
print(arr)