"""
Check whether binary tree is binary search tree
"""
from python.tree.node import Node


def is_bst_util(root):
    if root.left is None and root.right is None:
        return root.value, root.value, True

    left_max, left_min = root.value, root.value
    right_max, right_min = root.value, root.value

    if root.left:
        left_min, left_max, flag = is_bst_util(root.left)

        if not flag:
            return -1, -1, False

    if root.right:
        right_min, right_max, flag = is_bst_util(root.right)

        if not flag:
            return -1, -1, False

    return left_min, right_max, left_max <= root.value <= right_min


def is_bst(root):
    return is_bst_util(root)[2]


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

    print(is_bst(node4))
    node3.value, node2.value = node2.value, node3.value
    print(is_bst(node4))
