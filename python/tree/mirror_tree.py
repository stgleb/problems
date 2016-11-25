"""
Convert tree to mirror tree
"""
from python.tree.node import Node


def dfs(root):
    if root:
        dfs(root.left)
        print(root.value)
        dfs(root.right)


def mirror_tree(root):
    if root:
        mirror_tree(root.left)
        mirror_tree(root.right)
        root.left, root.right = root.right, root.left


def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.value == root2.value \
           and is_mirror(root1.left, root2.right) \
           and is_mirror(root1.right, root2.left)


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

    dfs(node4)
    mirror_tree(node4)
    dfs(node4)
