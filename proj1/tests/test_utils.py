from binarytree import BinaryTree
from binary_2tree import Binary2Tree
from prefix import Prefix


def __build_tree(tree):
    """
    :type tree: BinaryTree
    """

    tree.insert(Prefix('00'), 2)
    tree.insert(Prefix('10'), 2)
    tree.insert(Prefix('11'), 3)
    tree.insert(Prefix('010'), 3)
    tree.insert(Prefix('110'), 4)


def build_prof_tree():
    """
    :rtype : BinaryTree
    """
    tree = BinaryTree(1)
    __build_tree(tree)
    return tree


def build_prof_2tree():
    """
    :rtype : Binary2Tree
    """
    tree = Binary2Tree(1)
    __build_tree(tree)
    return tree


def find_height(root):
    """
    :type root: Node
    """
    if root is None:
        return 0

    left_height = find_height(root.left())
    right_height = find_height(root.right())

    return (left_height + 1) if left_height > right_height else (right_height + 1)


def __print_node(node, level):
    if node:

        # print right node
        __print_node(node.right, level + 1)

        # print the same number of tabs as the level of the node
        for i in range(0, 2*level):
            print('\t', end='')

        # print the node next-hop
        print(node)

        # print left node
        __print_node(node.left, level + 1)


def print_tree(tree):
    __print_node(tree.root, 0)


def print_tree_as_list(tree):
    node = tree.root
    nodes = []
    while node:

        # store the nodes children in the queue
        if node.left() is not None:
            nodes.insert(0, node.left())
        if node.right() is not None:
            nodes.insert(0, node.right())

        print("node: ", node)
        print("left: ", node.left())
        print("right: ", node.right())
        print()

        if len(nodes) == 0:
            # printed all nodes
            break

        # get next node in the queue
        node = nodes.pop()