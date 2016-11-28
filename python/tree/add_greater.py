"""
Add all greater values to every node in a given BST
"""
from python.tree.node import Node


def add_greater_util(root, value):
    if not root:
        return 0

    # Gather greater values from right subtree
    v = add_greater_util(root.right, value)
    # Add root.value to sum of right subtree and visa versa
    v += root.value
    root.value = v
    # Call passing sum of right subtree and current node value
    v = add_greater_util(root.left, v)

    return v


def add_greater(root):
    add_greater_util(root, 0)


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


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
    add_greater(node4)
    inorder_traversal(node4)
