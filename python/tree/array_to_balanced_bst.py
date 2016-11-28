"""
Convert sorted array to balanced binary search tree
"""

from python.tree.node import Node


def convert_util(arr, left, right):
    if left >= right:
        return None

    mid = (left + right) >> 1
    root = Node(arr[mid])

    root.left = convert_util(arr, left, mid)
    root.right = convert_util(arr, mid + 1, right)

    return root


def convert(arr):
    return convert_util(arr, 0, len(arr))


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = convert(arr)
    inorder_traversal(root)
