"""
Given an array with elements from 1 to n, but one is missing.
Find missing element.
"""


def find_missing_arithm(arr, n):
    total_sum = n * (n + 1)/2

    return total_sum - sum(arr)


def find_missing_xor(arr, n):
    total = 0
    actual = 0

    for i in range(1, n + 1):
        total ^= i

    for v in arr:
        actual ^= v

    return total ^ actual


if __name__ == "__main__":
    arr = [1, 2, 4, 6, 3, 7, 8]
    print(find_missing_arithm(arr, 8))
    print(find_missing_xor(arr, 8))
