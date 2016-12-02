"""
Given a binary tree, implement pre-order traversal without recursion.
"""
from python.tree.node import Node


def preorder_traversal(root):
    stack = [root]
    result = []

    while stack:
        cur = stack.pop()
        result.append(cur.value)

        if cur.right:
            stack.append(cur.right)

        if cur.left:
            stack.append(cur.left)

    return result


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
    print(preorder_traversal(node4))
