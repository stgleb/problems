"""
    Print last 6 digits of Fibbonachi number F(N)
    0 < N < 2 ^ 32
"""


def multiply(A, B):
    C = [[0, 0], [0, 0]]

    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    for i in range(len(C)):
        for j in range(len(C[i])):
            C[i][j] %= 1000000

    return C


def qpow(a, n):
    res = [[1, 1], [1, 0]]

    while n > 0:
        if n & 1 == 0:
            a = multiply(a, a)
            n >>= 1
        else:
            res = multiply(a, res)
            n -= 1

    return res


def solution(N):
    A = [[1, 1], [1, 0]]
    num = qpow(A, N)[1][1]

    return num


if __name__ == "__main__":
    print(solution(8))
