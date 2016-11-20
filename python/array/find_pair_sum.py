"""
Given an array pf numbers, find whether there is a pair
of numbers in the array whose sum is equal to K. Time complexity
O(N).
"""


def solution(A, K):
    d = dict()

    for v in A:
        d[v] = True
        tmp = K - v

        if tmp in d:
            return True

    return False


if __name__ == "__main__":
    A = [4, 1, 3, 8, 2, 8, 6, 7, 5]
    K = 11
    print(solution(A, K))
