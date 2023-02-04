# список реализованных сортировок

# сортировка простыми вставками
def insert_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# быстрая сортировка
def quick_sort(arr, start, end):
    # реализация, где мы берём первый и последний индексы подмассива, который будет сортироваться
    if start >= end:
        return

    i = start
    j = end
    p = arr[start + (end - start) // 2]

    while i <= j:
        while arr[i] < p:
            i += 1
        while arr[j] > p:
            j -= 1
        if i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

            i += 1
            j -= 1

    if start < j:
        quick_sort(arr, start, j)
    if end > i:
        quick_sort(arr, i, end)


# сортировка слиянием
def merge(arr, low, mid, high):
    buff = [None] * (high + 1 - low)

    h = 0
    i = low
    j = mid + 1

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            buff[h] = arr[i]
            i += 1
        else:
            buff[h] = arr[j]
            j += 1
        h += 1

    if i > mid:
        for k in range(j, high + 1):
            buff[h] = arr[k]
            h += 1
    else:
        for k in range(i, mid + 1):
            buff[h] = arr[k]
            h += 1

    for k in range(0, high - low + 1):
        arr[low + k] = buff[k]


def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
