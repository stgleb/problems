"""
Given an 2d array with numbers - prices,
you can move from (0, 0) to (n, m) only right or down,
find path of maximum cost.
"""


def prepare_array(arr):
    for i in range(1, len(arr[0])):
        arr[0][i] += arr[0][i - 1]

    for j in range(1, len(arr)):
        arr[j][0] += arr[j - 1][0]


def find_path(arr):
    prepare_array(arr)
    path = []
    n = len(arr)
    m = len(arr[0])
    x, y = n - 1, m - 1

    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            if arr[i - 1][j] > arr[i][j - 1]:
                arr[i][j] += arr[i - 1][j]
            else:
                arr[i][j] += arr[i][j - 1]

    while x > 0 and y > 0:
        if arr[x - 1][y] > arr[x][y - 1]:
            path.append((x - 1, y))
            x -= 1
        else:
            path.append((x, y - 1))
            y -= 1

    while x > 0:
        path.append((x - 1, 0))
        x -= 1

    while y > 0:
        path.append((0, y - 1))
        y -= 1

    return arr[n - 1][m - 1], path[::-1]


if __name__ == "__main__":
    arr = [
        [2, 3, 1, 4, 6],
        [7, 10, 3, 6, 8],
        [4, 4, 5, 2, 1],
        [7, 6, 4, 3, 9]
    ]

    print(find_path(arr))
