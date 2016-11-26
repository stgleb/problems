"""
Given an array where all elements occurred twice except one.
"""


def find_unique(arr):
    total = 0

    for v in arr:
        total ^= v

    return total


if __name__ == "__main__":
    arr = [2, 3, 1, 2, 5, 5, 4, 6, 4, 6]
    print(find_unique(arr))
