"""
Check whether tree is balanced
"""
from python.tree.node import Node


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1


def is_balanced_naive(root):
    lh = height(root.left)
    rh = height(root.right)

    if lh > rh * 2 or lh * 2 < rh:
        return False

    return True


def is_balanced_util(root):
    if root is None:
        return 0, True

    lh, _ = is_balanced_util(root.left)
    rh, _ = is_balanced_util(root.right)

    h = max(lh, rh) + 1

    if lh > rh * 2 or lh * 2 < rh:
        return h, False

    return h, True


def is_balanced(root):
    return is_balanced_util(root)[1]


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node0 = Node(0)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node5

    print(is_balanced_naive(node4))
    print(is_balanced(node4))
    node1.left = node0
    print(is_balanced_naive(node4))
    print(is_balanced(node4))
