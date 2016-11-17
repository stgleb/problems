"""
Find smallest subarray with given sum
"""


def find_subaray(arr, target):
    l, r = 0, 0
    sum = 0
    min_size = len(arr)
    min_l = 0
    min_r = 0

    while r < len(arr):
        sum += arr[r]
        r += 1

        while sum > target:
            sum -= arr[l]
            l += 1

        if sum == target:
            if r - l < min_size:
                min_size = r - l
                min_l = l
                min_r = r

    return min_l, min_r


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 4, 2]
    l, r = find_subaray(arr, 6)
    print(arr[l: r])
