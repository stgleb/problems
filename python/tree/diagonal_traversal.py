from python.tree.node import Node


def traverse(root, value, view):
    if root is None:
        return

    if value in view:
        view[value].append(root.value)
    else:
        view[value] = [root.value]

    traverse(root.left, value + 1, view)
    traverse(root.right, value, view)


def diagonal_view(root):
    """
    Computes diagonal representation of tree


            8
          /   \
        3     10
       / \      \
      1  6      14
        / \      /
       4   7    13

    Output:

    8, 10, 14
    3, 6, 7, 13
    1, 4

    :param root:
    :return:
    """
    diagonal_map = dict()
    traverse(root, 0, diagonal_map)

    return diagonal_map


def test():
    node1 = Node(1)
    node3 = Node(3)
    node4 = Node(4)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node10 = Node(10)
    node13 = Node(13)
    node14 = Node(14)

    node8.left = node3
    node8.right = node10
    node3.left = node1
    node3.right = node6
    node6.left = node4
    node6.right = node7
    node10.right = node14
    node14.left = node13

    expected_result = {
        0: [8, 10, 14],
        1: [3, 6, 7, 13],
        2: [1, 4]
    }

    actual_result = diagonal_view(node8)

    assert expected_result == actual_result


if __name__ == "__main__":
    test()








