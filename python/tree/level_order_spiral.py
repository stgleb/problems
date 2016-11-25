"""
Given a tree, print level order traversal in spiral form

      4
    /  \
   2    5
  / \    \
 1   3    6

  [4]
  [2, 5]
  [6, 3, 1]
"""
from python.tree.node import Node


def level_order_traversal_spiral(root):
    stack1 = [root]
    stack2 = []
    level = 0
    levels = {}
    direction = True

    while stack1:
        levels[level] = [node.value for node in stack1]

        while stack1:
            if direction:
                cur = stack1[0]
                stack1 = stack1[1:]

                if cur.left:
                    stack2.append(cur.left)

                if cur.right:
                    stack2.append(cur.right)
            else:
                cur = stack1.pop()

                if cur.right:
                    stack2.append(cur.right)

                if cur.left:
                    stack2.append(cur.left)

        direction = not direction
        stack1 = stack2[:]
        stack2 = []
        level += 1

    return levels, level


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node5
    node5.right = node6
    levels, level_count = level_order_traversal_spiral(node4)

    for i in range(level_count):
        print(levels[i])
