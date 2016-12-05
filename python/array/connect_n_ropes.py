"""
There are given n ropes of different lengths, we need to connect these
ropes into one rope. The cost to connect two ropes is equal to sum of
their lengths. We need to connect the ropes with minimum cost.
"""


from heapq import heappop as pop
from heapq import heappush as push


def connect_n_ropes(ropes):
    heap = []

    for r in ropes:
        push(heap, r)

    while len(heap) > 1:
        first = pop(heap)
        second = pop(heap)
        push(heap, first + second)

    return heap[0]


if __name__ == "__main__":
    ropes = [5, 4, 1, 2, 3, 9, 6]
    print(connect_n_ropes(ropes))
