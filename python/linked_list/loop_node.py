"""
Find node when loop begins
"""
from python.linked_list import Node


def find_loop_node(head):
    fast, slow = head.next, head

    while fast is not None and \
                    fast.next is not None \
            and fast != slow:
        fast = fast.next.next
        slow = slow.next

    if slow == fast:
        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow.value

    return None


if __name__ == "__main__":
    node5 = Node(5)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)
    node5.next = node4

    print(find_loop_node(node1))
