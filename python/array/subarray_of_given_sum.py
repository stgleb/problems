"""
Given an array, find subarray with given sum
"""


def find_subarray(arr, target):
    l, r = 0, 0
    sum = 0

    while r < len(arr):
        sum += arr[r]
        r += 1

        while sum > target:
            sum -= arr[l]
            l += 1

        if sum == target:
            return l, r

    return -1, -1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 4, 2]
    l, r = find_subarray(arr, 6)
    print(arr[l: r])
