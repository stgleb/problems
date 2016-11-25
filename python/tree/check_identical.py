"""
Check if two trees are identical
"""
from python.tree.node import Node


def check_identical(root1, root2):
    """
    Check if two trees are identical
    :param root1:
    :param root2:
    :return:
    """
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    return root1.value == root2.value and \
           check_identical(root1.left, root2.left) \
           and check_identical(root1.right, root2.right)


def check_identical_iteratively(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    stack1 = [root1]
    stack2 = [root2]

    while stack1 and stack2:
        root1 = stack1.pop()
        root2 = stack2.pop()

        if root1 is None and root2 is None:
            continue

        if root1 is None or root2 is None:
            return False

        if root1.value != root2.value:
            return False

        stack1.append(root1.right)
        stack1.append(root1.left)

        stack2.append(root2.right)
        stack2.append(root2.left)

    return True


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

    node11 = Node(1)
    node12 = Node(2)
    node13 = Node(3)
    node14 = Node(4)
    node15 = Node(5)

    node14.left = node12
    node12.left = node11
    node12.right = node13
    node14.right = node15

    print(check_identical(node4, node14))
    print(check_identical(node4, node4))
    print(check_identical_iteratively(node4, node14))
    print(check_identical_iteratively(node4, node4))

