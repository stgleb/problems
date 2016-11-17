"""
Given an array, find subarray with given sum
"""


def find_subarray(arr, target):
    l, r = 0, 0
    sum = 0

    for i in range(len(arr)):
        if sum < target:
            sum += arr[r]
        elif sum > target:
            sum -= arr[l]
            l += 1
        else:
            return l, r

        r += 1

    return -1, -1

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 4, 2]
    l, r = find_subarray(arr, 6)
    print(arr[l: r])
