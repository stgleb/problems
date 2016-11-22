"""
Select a random node from single linked list with only one traversal
"""
import random
from python.linked_list import Node


def get_random(head):
    cur = head
    count = 0
    result = None

    while cur != None:
        count += 1

        if random.randrange(count) == 0:
            result = cur

        cur = cur.next

    return result.value


def test_get_random(head, N):
    freq = dict()

    for i in range(N):
        result = get_random(head)

        if result not in freq:
            freq[result] = 1
        else:
            freq[result] += 1

    return {key: float(value) / N for key, value in freq.items()}


if __name__ == "__main__":
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    N = 10000
    print(test_get_random(node1, N))
