"""
Find magic index where A[i] == i
"""


def find_magic_index_util(arr, left, right):
    mid = (left + right) >> 1

    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return find_magic_index_util(arr, left, mid)
    else:
        return find_magic_index_util(arr, mid, right)


def find_magic_index(arr):
    return find_magic_index_util(arr, 0, len(arr))


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, 4, 7, 9, 10, 13, 15]
    print(find_magic_index(arr))
