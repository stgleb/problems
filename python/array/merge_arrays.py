"""
Given two sorted arrays A and B, A has a buffer at the end of size B.
Merge two arrays.
"""


def merge(A, B, n, m):
    i = n - 1
    j = m - 1
    k = len(A) - 1

    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

    while i >= 0:
        A[k] = A[i]
        i -= 1
        k -= 1

    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1

    return A


if __name__ == "__main__":
    A = [1, 3, 5, 6, 7, 8, -1, -1, -1, -1]
    B = [2, 4, 9, 10]
    print(merge(A, B, 6, 4))
