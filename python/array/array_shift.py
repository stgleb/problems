"""
A zero-indexed array A consisting of N integers is given. Rotation of the
array means that each element is shifted right by one index, and the last element
of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7].
The goal is to rotate array A K times; that is, each element of A will be
shifted to the right by K indexes.

Write a function:

object Solution { def solution(a: Array[Int], k: Int): Array[Int] }

that, given a zero-indexed array A consisting of N integers and an integer K,
returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].
"""


def _shift(A):
    tmp = A[len(A) - 1]

    for i in range(len(A) - 2, -1, -1):
        A[i + 1] = A[i]

    A[0] = tmp


def shift_array(A, K):
    """
    The simplest solution
    :param A:
    :param K:
    :return:
    """
    for i in range(K):
        _shift(A)


def array_shift_functional(A, K):
    n = len(A)
    return [A[(index - K) % n] for index, value in enumerate(A)]


if __name__ == "__main__":
    A = [3, 8, 9, 7, 6]
    print(array_shift_functional(A, 3))
    shift_array(A, 3)
    print(A)
