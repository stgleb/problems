"""
Reverse single linked list
"""
from python.linked_list import Node


def reverse(head):
    cur = head
    nxt = cur.next
    prev = None

    while nxt is not None:
        cur.next = prev
        prev = cur
        cur = nxt
        nxt = nxt.next

    cur.next = prev

    return cur

if __name__ == "__main__":
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    new_head = reverse(node1)

    while new_head is not None:
        print(new_head.value)
        new_head = new_head.next
