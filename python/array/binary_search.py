"""
Implement binary search algorithm
"""


def search_util(a, l, r, val):
    if l < r:
        mid = (l + r) >> 1

        if a[mid] == val:
            return mid
        elif a[mid] < val:
            return search_util(a, mid + 1, r, val)
        elif a[mid] > val:
            return search_util(a, l, mid - 1, val)


def binary_search(a, val):
    l, r = 0, len(a)

    while l < r:
        mid = (l + r) >> 1

        if a[mid] == val:
            return mid
        elif a[mid] < val:
            l = mid
        elif a[mid] > val:
            r = mid


def search(a, val):
    """
    Return index of val or None
    :param a: array
    :param val: value to search
    :return: index or None
    """
    return search_util(a, 0, len(a), val)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(search(a, 8))
    print(binary_search(a, 1))

