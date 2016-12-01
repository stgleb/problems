"""
Convert sorted ddl to binary search tree
"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def find_mid(left, right):
    slow = left
    fast = left

    while fast != right:
        fast = fast.next

        if fast == right:
            slow = slow.next
            break

        fast = fast.next
        slow = slow.next

    return slow


def convert(head, tail):
    if head == tail:
        head.next = None
        head.prev = None
        tail.next = None
        tail.prev = None
        return head

    mid = find_mid(head, tail)
    root = mid

    if head != mid:
        left_root = convert(head, mid.prev)
    else:
        left_root = None

    if mid != tail:
        right_root = convert(mid.next, tail)
    else:
        right_root = None

    root.prev = left_root
    root.next = right_root

    return root


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.prev)
    print(root.value)
    inorder_traversal(root.next)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6

    node6.prev = node5
    node5.prev = node4
    node4.prev = node3
    node3.prev = node2
    node2.prev = node1

    root = convert(node1, node5)
    inorder_traversal(root)

