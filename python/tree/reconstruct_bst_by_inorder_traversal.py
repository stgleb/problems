"""
Given in-order traversal of binary search tree, reconstruct original tree.
"""


from python.tree.node import Node


def reconstruct(arr):
    if not arr:
        return

    mid = len(arr) >> 1
    root_value = arr[mid]
    root = Node(root_value)

    root.left = reconstruct(arr[:mid])
    root.right = reconstruct(arr[mid + 1:])

    return root


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


if __name__ == "__main__":
    arr = [1, 5, 7, 10, 40, 50]
    root = reconstruct(arr)
    inorder_traversal(root)
