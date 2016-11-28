"""
Given node in binary tree, find in-order successor if parent pointer is
given.
"""


class Node(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def find_successor(node):
    if node.right is None:
        parent = node.parent
        cur = node

        while parent is not None and parent.right == cur:
            cur = parent
            parent = parent.parent

        if parent is None:
            return None

        return parent.value
    else:
        cur = node.right

        while cur.left:
            cur = cur.left

        return cur.value


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node4.left = node2
    node2.parent = node4
    node2.left = node1
    node1.parent = node2
    node2.right = node3
    node3.parent = node2
    node4.right = node5
    node5.parent = node4

    print(find_successor(node2))
