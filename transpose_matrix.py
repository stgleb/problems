"""
Transpose e.g rotate by 90 degrees matrix in place
"""


def transponse(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A[i])):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    return A


if __name__ == "__main__":
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    transponse(A)

    for row in A:
        print(row)


