arr = [0.3,-0.2,0.4,-0.1,-0.2,0.5,-0.3,0.6]

def maxCrossSum(arr,low,mid,high):
    leftSum = -1000000
    rightSum = -1000000

    sum =0
    for i in range(mid,low-1,-1):
        sum+=arr[i]
        if sum>leftSum:
            leftSum = sum

    sum = 0
    for i in range(mid+1,high+1):
        sum+=arr[i]
        if sum>rightSum:
            rightSum = sum

    return leftSum + rightSum

def maxSubArraySum(arr,low,high):
    if low == high:
        return arr[low]
    mid = (low+high)//2
    lss = maxSubArraySum(arr,low,mid)
    rss = maxSubArraySum(arr,mid+1,high)
    css = maxCrossSum(arr,low,mid,high)

    return max(lss,rss,css)


print(maxSubArraySum(arr, 0, len(arr) - 1))
