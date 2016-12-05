"""
Given a binary search tree, count number of nodes which
values are in given range.
"""
from python.tree.node import Node


def get_count(root, left, right):
    if not root:
        return 0

    if root.value <= right and root.value >= left:
        return get_count(root.left, left, right) + \
               get_count(root.right, left, right) + 1
    elif root.value < left:
        return get_count(root.right, left, right)
    elif root.value > right:
        return get_count(root.left, left, right)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node5
    print(get_count(node4, 3, 7))
