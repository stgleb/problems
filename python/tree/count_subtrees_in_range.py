"""
Given a Binary Search Tree (BST) of integer values and a range [low, high],
 return count of nodes where all the nodes under that node (or subtree rooted
with that node) lie in the given range
"""
from python.tree.node import Node


def count_subtrees_util(root, left, right):
    if not root:
        return 0, True

    lcount, lresult = count_subtrees_util(root.left, left, right)
    rcount, rresult = count_subtrees_util(root.right, left, right)

    if lresult and rresult and root.value <= right and root.value >= left:
        return lcount + rcount + 1, True

    return lcount + rcount, False


def count_subtrees(root, left, right):
    count, _ = count_subtrees_util(root, left, right)

    return count

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node50 = Node(50)
    node40 = Node(40)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node5
    node4.right = node40
    node40.right = node50
    node40.left = node5
    print(count_subtrees(node4, 1, 45))
