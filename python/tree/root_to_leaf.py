from python.tree.node import Node


def root_to_leaf(root, parent):
    root.parent = parent

    if root.left is None and root.right is None:
        result = [root.value]

        while parent:
            result.append(parent.value)
            parent = parent.parent

        print result

    if root.left is not None:
        root_to_leaf(root.left, root)

    if root.right is not None:
        root_to_leaf(root.right, root)


if __name__ == "__main__":
    node1 = Node(1)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.left = node3
    node1.right = node4
    node4.right = node5

    root_to_leaf(node1, None)
