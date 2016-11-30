"""
Given an array of numbers, segregate odd and even numbers

Example:

    3, 4, 1, 9, 5, 2

    4, 2, 1, 3, 9, 5
"""


def segregate(arr):
    tail = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[tail], arr[i] = arr[i], arr[tail]
            tail += 1

    arr[tail], arr[i] = arr[len(arr) - 1], arr[tail]
    return arr


if __name__ == "__main__":
    arr = [3, 4, 1, 9, 5, 2]
    print(segregate(arr))
