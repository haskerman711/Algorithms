def insertion_sort(arr, n):
    for i in range(n-1):
        j = i + 1
        temp = arr[j]
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
