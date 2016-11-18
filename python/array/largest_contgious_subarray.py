"""
Write an efficient program to find the sum of contiguous subarray
within a one-dimensional array of numbers which has the largest sum.
"""


def subarray(arr):
    sum = 0
    begin = 0
    end = 0

    for i in range(len(arr)):
        if sum < 0:
            begin = i
            end = i
            sum = 0
        elif sum + arr[i] > sum:
            end = i

        sum += arr[i]

    return begin, end


if __name__ == "__main__":
    arr = [-2, -3, -4, -1, -2, -1, -5, -3]
    print(subarray(arr))
