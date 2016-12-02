"""
Given in-order traversal of binary search tree, reconstruct original tree.
"""


from python.tree.node import Node



def reconstruct(arr):
    pass


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


if __name__ == "__main__":
    arr = [10, 5, 1, 7, 40, 50]
    root = reconstruct(arr)
    inorder_traversal(root)
