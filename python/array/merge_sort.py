def merge(arr, tmp, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = tmp[i]


def _merge_sort(arr, tmp, left, right):
    if left < right:
        mid = (left + right) / 2
        _merge_sort(arr, tmp, left, mid)
        _merge_sort(arr, tmp, mid + 1, right)
        merge(arr, tmp, left, mid, right)

    return arr


def merge_sort(arr):
    tmp = [0 for x in arr]
    return _merge_sort(arr, tmp, 0, len(arr) - 1)


if __name__ == "__main__":
    arr = [4, 1, 7, 5, 8, 9, -1, -2]
    print(merge_sort(arr))
