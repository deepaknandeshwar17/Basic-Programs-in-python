def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right)//2
        if arr[mid]== target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [29,293,48,504,492,889,37662,948472,28283634546]
target = 889
print(binary_search(arr, target))