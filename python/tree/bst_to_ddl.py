"""
Convert binary search tree to double linked list
"""
from python.tree.node import Node


def convert(root):
    if root is None:
        return root, root

    left_left, left_right = convert(root.left)
    right_left, right_right = convert(root.right)

    if root.left is None:
        left_left, left_right = root, root
    else:
        left_right.left = root
        root.right = left_right

    if root.right is None:
        right_right, right_left = root, root
    else:
        right_left.right = root
        root.left = right_left

    return left_left, right_right


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
    head, tail = convert(node4)

    while head is not None:
        print(head.value)
        head = head.left
