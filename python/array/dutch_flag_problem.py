"""
Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[].
The functions should put all 0s first, then all 1s and all 2s in last.

Example
Input = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

"""


def dutch_sort(arr):
    left, right = 0, len(arr) - 1
    cur = 0

    while cur <= right:
        if arr[cur] == 0:
            arr[cur], arr[left] = arr[left], arr[cur]
            left += 1
            cur += 1
        elif arr[cur] == 2:
            arr[cur], arr[right] = arr[right], arr[cur]
            right -= 1
        else:
            cur += 1

    return arr


if __name__ == "__main__":
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    print(dutch_sort(arr))
