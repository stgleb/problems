"""
Given a binary tree, the task is to flip the binary tree towards right
direction that is clockwise.  See below examples to see the transformation.


        4
       / \
      2   5
     / \
    1   3


        1
       / \
      3   2
         / \
        5   4

"""
from python.tree.node import Node


def inorder_traversal(root):
    if not root:
        return

    inorder_traversal(root.left)
    print(root.value)
    inorder_traversal(root.right)


def flip_tree(root):
    if not root:
        return

    flip_tree(root.left)

    if root.left:
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None


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
    inorder_traversal(node4)
    flip_tree(node4)
    print("-----------------")
    inorder_traversal(node1)

