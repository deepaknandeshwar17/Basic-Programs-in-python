def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] =