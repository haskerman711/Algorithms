# merge_sort.py

import random


def merge(arr, l, m, r):
    l_arr = arr[l:m+1] + [float("inf"),]
    r_arr = arr[m+1: r+1] + [float("inf"),]
    l_i = 0
    r_i = 0
    for i in range(l, r+1):
        if l_arr[l_i] < r_arr[r_i]:
            arr[i] = l_arr[l_i]
            l_i += 1
        else:
            arr[i] = r_arr[r_i]
            r_i += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


def verify():
    try:
        for i in range(100):
            arr = [random.randint(0, 100) for _ in range(100)]
            arr_ = arr[:]
            #
            arr.sort()
            merge_sort(arr_, 0, len(arr_) - 1)
            # check
            assert arr == arr_, f"{arr}\n{arr_}"
    except AssertionError:
        print("Error")
    print("OK")


if __name__ == "__main__":
    verify()