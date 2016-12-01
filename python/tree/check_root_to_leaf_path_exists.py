"""
Given a binary tree and an array, the task is to find if the given array
sequence is present as a root to leaf path in given tree.
"""
from python.tree.node import Node


def check_exists(root, path):
    if not root and not path:
        return True

    if not root or not path:
        return False

    if root.value != path[0]:
        return False
    
    if path[0] == root.value:
        return check_exists(root.left, path[1:]) or \
               check_exists(root.right, path[1:])


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

    print(check_exists(node4, [4, 5]))
    print(check_exists(node4, [4, 2, 3]))
    print(check_exists(node4, [4, 2, 1]))
    print(check_exists(node4, [4, 2, 5]))
    print(check_exists(node4, [4, 5, 3]))
    print(check_exists(node4, [1, 2, 3]))
