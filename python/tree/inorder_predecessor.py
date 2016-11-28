"""
Given node in binary tree, find in-order predecessor if parent pointer is
given.
"""


class Node(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def find_predecessor(node):
    if node.left:
        cur = node.left

        while cur.right:
            cur = cur.right

        return cur.value
    else:
        cur = node
        parent = node.parent

        while parent is not None and cur.parent == parent.left:
            cur = parent
            parent = parent.parent

        if parent is None:
            return None

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

    print(find_predecessor(node3))
