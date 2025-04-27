arr = [1,3,4,7,9,12,14,16,18,21,22,28,31]

def binarySearch(arr,x,low,high):
    mid = (low+high)//2
    if arr[mid]==x:
        return mid
    elif x < arr[mid]:
        return binarySearch(arr,x,low,mid-1)
    elif x> arr[mid]:
        return binarySearch(arr,x,mid+1,high)
    return -1

print(binarySearch(arr,14,0,len(arr)-1))