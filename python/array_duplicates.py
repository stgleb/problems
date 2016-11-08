"""
    Find any duplicate element in the array, if there are no element greater than
    length of an array.
"""


def find_duplicate(arr):
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[arr[i]] == arr[i]:
                return arr[i]
            else:
                buf = arr[i]
                arr[i] = arr[arr[i]]
                arr[buf] = buf

    return None


if __name__ == "__main__":
    arr = [0, 1, 3, 4, 2]
    print find_duplicate(arr)
