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
        root.left, root.right = root.right, root.left
        mirror_tree(root.left)
        mirror_tree(root.right)


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
