"""
Print level order traversal of binary tree

      4
    /  \
   2    5
  / \    \
 1   3    6

  [4]
  [2, 5]
  [1, 3, 6]
"""
from python.tree.node import Node


def level_order_traversal(root):
    q1 = [root]
    q2 = []
    levels = {}
    level = 0

    while q1:
        levels[level] = [node.value for node in q1]

        while q1:
            cur = q1[0]
            q1 = q1[1:]

            if cur.left:
                q2.append(cur.left)

            if cur.right:
                q2.append(cur.right)

        q1 = q2[:]
        q2 = []
        level += 1

    return levels, level


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
    levels, level_count = level_order_traversal(node4)

    for i in range(level_count):
        print(levels[i])
