"""
Count inversions in an array, inversion when for i,j where i < j
a[i] > a[j]
"""


def merge(arr, tmp, left, mid, right):
    i = left
    j = mid
    k = left
    inv_count = 0

    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            tmp[k] = arr[i]
            i += 1
        else:
            tmp[k] = arr[j]
            inv_count += mid - i
            j += 1
        k += 1

    while i < mid:
        tmp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = tmp[i]

    return inv_count


def _merge_sort(arr, tmp, left, right):
    inv_count = 0

    if left < right:
        mid = (right + left) / 2
        inv_count += _merge_sort(arr, tmp, left, mid)
        inv_count += _merge_sort(arr, tmp, mid + 1, right)
        inv_count += merge(arr, tmp, left, mid+1, right)

    return inv_count


def merge_sort(arr):
    tmp = [0 for x in range(len(arr))]
    return _merge_sort(arr, tmp, 0, len(arr) - 1)


def count_inversions(arr):
    return merge_sort(arr)


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    print(count_inversions(arr))
