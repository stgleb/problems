"""
Find K largest elements in stream of integers
"""


from heapq import heappop as pop
from heapq import heappush as push


def k_largest(stream, k):
    q = []

    for elem in stream:
        if len(q) < k:
            push(q, elem)
        elif q[0] < elem:
            pop(q)
            push(q, elem)

    return q


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 6, 9, 7, 4, 11, 5]
    print(k_largest(arr, 3))
