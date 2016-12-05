"""
Given an sorted array, rotated unknown amount of times.
Find an element in there in O(LogN)
"""


def search_util(a, left, right, val):
    if left < right:
        mid = (left + right) >> 1

        # val is found
        if a[mid] == val:
            return mid
        # Left side is sorted
        elif a[left] < a[mid]:
            # Val in left side
            if a[left] < val < a[mid]:
                return search_util(a, left, mid - 1, val)
            else:
                # Val is in right side
                return search_util(a, mid + 1, right, val)
        else:
            # Right side is sorted
            if a[mid] < val < a[right]:
                return search_util(a, mid + 1, right, val)
            else:
                return search_util(a, left, mid - 1, val)


def search(a, val):
    return search_util(a, 0, len(a) - 1, val)


if __name__ == "__main__":
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(search(arr, 1))
    print(search(arr, 5))
    print(search(arr, 10))
