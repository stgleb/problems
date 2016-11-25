from python.tree.node import Node


def tree_size(root):
    if not root:
        return 0

    return tree_size(root.left) + tree_size(root.right) + 1


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
    print(tree_size(node4))
