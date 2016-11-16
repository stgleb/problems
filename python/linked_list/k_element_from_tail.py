"""
Find element on k-th position from list tail
"""
from python.linked_list import Node


def kth_element(head, k):
    first = head
    second = head
    cnt = 0

    while first is not None and cnt < k:
        first = first.next
        cnt += 1

    while first is not None:
        first = first.next
        second = second.next

    return second


if __name__ == "__main__":
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    print(kth_element(node1, 2).value)
