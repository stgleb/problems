"""
Given preorder traversal of a binary search tree, construct the BST.
"""

from python.tree.node import Node


def reconstruct(arr):
    if not arr:
        return

    root = Node(arr[0])

    i = 1

    while i < len(arr[1:]) and arr[i] < arr[0]:
        i += 1

    left_root = reconstruct(arr[1:i])
    right_root = reconstruct(arr[i:])

    root.left = left_root
    root.right = right_root

    return root


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def preorder_traversal(root):
    if not root:
        return

    print(root.value)
    preorder_traversal(root.left)
    preorder_traversal(root.right)


if __name__ == "__main__":
    arr = [10, 5, 1, 7, 40, 50]
    root = reconstruct(arr)
    inorder_traversal(root)
    print("---------------------")
    preorder_traversal(root)

