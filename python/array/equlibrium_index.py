"""
Equilibrium index of an array is an index such that the sum of elements
at lower indexes is equal to the sum of elements at higher indexes.
"""


def find_equlibrium(arr):
    left_sum = 0
    total = sum(arr)

    for i in range(len(arr) - 1, -1, -1):
        left_sum += arr[i]

        if total - left_sum == left_sum:
            return arr[:i], arr[i:]


if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print(find_equlibrium(arr))

    arr = [1, 2, 5, 2, 4, 4, 2]
    print(find_equlibrium(arr))
