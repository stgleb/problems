"""
Find duplicates in an array where elements in range [0, n - 1], with O(N)
complexity and O(1) extra space.
"""


def find_duplicates(arr):
    duplicates = []

    for i in range(len(arr)):
        # Set value on corresponding index to negative
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] *= -1
        else:
            duplicates.append(abs(arr[i]))

    return duplicates


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 2, 6, 6]
    print(find_duplicates(arr))
