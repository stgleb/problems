"""
Given an array with duplicates, find first occurrence of median element
"""


def find_median(arr):
    first_indexes = []
    i = 0

    while i < len(arr):
        first_indexes.append(i)

        while i + 1 < len(arr) and arr[i] == arr[i + 1]:
            i += 1

        i += 1

    return arr[first_indexes[len(first_indexes) / 2]]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7]
    print(find_median(arr))
