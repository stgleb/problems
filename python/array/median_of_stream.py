"""
Given that integers are read from a data stream. Find median of elements
read so for in efficient way.
"""


from heapq import heappop as pop
from heapq import heappush as push


def sliding_median(stream):
    small, big = [], []
    median = []

    for val in stream:
        if not small and not big:
            push(big, val)

        if val > big[0]:
            push(big, val)
        elif val < big[0]:
            push(small, -val)

        if len(big) > len(small) + 1:
            val = pop(big)
            push(small, -val)
        elif len(small) >= len(big):
            val = pop(small)
            push(big, -val)

        if big:
            median.append(big[0])

    return median


if __name__ == "__main__":
    arr = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]
    print(sliding_median(arr))
