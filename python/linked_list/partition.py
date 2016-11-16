"""
Make a partition around given element of lined list
"""

from python.linked_list import Node


def partition(head, value):
    first, last = head, head

    while first.next is not None:
        if first.value >= value:
            first = first.next
        else:
            last.value, first.value = first.value, last.value
            last = last.next
            first = first.next

    last.value, first.value = first.value, last.value


if __name__ == "__main__":
    node5 = Node(2)
    node4 = Node(1, node5)
    node3 = Node(3, node4)
    node2 = Node(5, node3)
    node1 = Node(4, node2)
    partition(node1, 2)
    cur = node1

    while cur is not None:
        print(cur.value)
        cur = cur.next


