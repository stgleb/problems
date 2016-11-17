"""
Given an array and grasshopper on the first element.
Grasshopper on i-th index can jump to maximum a[i] cells.
Calculate an optimal path of grasshopper from 0 to N.
"""


def find_path(arr):
    pth = [len(arr) for _ in range(len(arr))]
    jumps = [len(arr) for _ in range(len(arr))]
    jumps[0] = 0

    for i in range(len(arr)):
        cnt = arr[i]

        for j in range(i + 1, min(len(arr) - 1, cnt + i) + 1):
            if jumps[i] + 1 < jumps[j]:
                jumps[j] = jumps[i] + 1
                pth[j] = i

    path = [len(arr) - 1]
    j = pth[len(pth) - 1]

    while j != 0:
        path = [j] + path
        j = pth[j]

    path = [j] + path

    return jumps[len(arr) - 1], path


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    print(find_path(arr))
