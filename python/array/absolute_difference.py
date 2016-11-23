"""
Given a sorted array of distinct elements, the task is to find the summation
of absolute differences of all pairs in the given array

Input : arr[] = {1, 2, 3, 4}
Output: 10
Sum of |2-1| + |3-1| + |4-1| +
       |3-2| + |4-2| + |4-3| = 10

Input : arr[] = {1, 8, 9, 15, 16}
Output: 74

Input : arr[] = {1, 2, 3, 4, 5, 7, 9, 11, 14}
Output: 188

"""


def abs_difference(a):
    sum = 0
    n = len(a) - 1

    for i in range(n, -1,  -1):
        sum += a[i] * i - a[i] * (n - i - 1)

    return sum / 2


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(abs_difference(a))
