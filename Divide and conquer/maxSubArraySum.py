def maxCrossingSum(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    max_left = mid

    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i

    right_sum = float('-inf')
    total = 0
    max_right = mid + 1

    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i

    return (left_sum + right_sum, max_left, max_right)


def maxSubArraySum(arr, low, high):
    if low == high:
        return (arr[low], low, high)

    mid = (low + high) // 2

    left_sum, left_low, left_high = maxSubArraySum(arr, low, mid)
    right_sum, right_low, right_high = maxSubArraySum(arr, mid + 1, high)
    cross_sum, cross_low, cross_high = maxCrossingSum(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_sum, left_low, left_high)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_sum, right_low, right_high)
    else:
        return (cross_sum, cross_low, cross_high)


arr = [-10, 5, 3, -4, 2, -3, 7, 1, 2, -5]
max_sum, start, end = maxSubArraySum(arr, 0, len(arr) - 1)
print("Maximum subarray sum:", max_sum)
print("Subarray indices:", start, "to", end)
print("Subarray:", arr[start:end + 1])


def maxCrossingSumOnly(arr, low, mid, high):
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total

    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def maxSubArraySumOnly(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2
    left = maxSubArraySumOnly(arr, low, mid)
    right = maxSubArraySumOnly(arr, mid + 1, high)
    cross = maxCrossingSumOnly(arr, low, mid, high)

    return max(left, right, cross)

arr = [-10, 5, 3, -4, 2, -3, 7, 1, 2, -5]
print("Maximum subarray sum (sum only):", maxSubArraySumOnly(arr, 0, len(arr) - 1))




