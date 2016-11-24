"""
Given two binary trees T1 and T2, check whether one is subtree of another
"""
from python.tree.node import Node


def check_subtree_util(root1, root2=None):
    if root2 is None:
        return True

    if root1 is None:
        return False

    return (check_subtree_util(root1.left, root2.right)
            or check_subtree_util(root1.right, root2.right)) \
            and root1.value == root2.value


def check_subtree(root1, root2):
    if root1 is None:
        return False

    if check_subtree_util(root1, root2):
        return True

    return (check_subtree_util(root1.left, root2) or
            check_subtree_util(root1.right, root2))


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

    node11 = Node(1)
    node12 = Node(2)
    node13 = Node(3)

    node12.left = node11
    node12.right = node13

    print(check_subtree(node4, node12))
