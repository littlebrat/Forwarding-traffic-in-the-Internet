from proj1.binary_2tree.binary_2tree import Binary2Tree
from proj1.binary_tree.binarytree import BinaryTree
from proj1.prefix import Prefix
from proj1.node import Node


def find_height(root):
    """
    :type root: Node
    """
    if root is None:
        return 0
    
    left_height = find_height(root.left())
    right_height = find_height(root.right())
    
    return (left_height + 1) if left_height > right_height else (right_height + 1)


def print_node(node, level):
    if node:

        # print right node
        print_node(node.right(), level + 1)

        # print the same number of tabs as the level of the node
        for i in range(0, 2*level):
            print('\t', end='')

        # print the node next-hop
        print(node)

        # print left node
        print_node(node.left(), level + 1)


def print_tree(tree):
    print_node(tree.root, 0)


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


def test_insert(tree):
    print("INSERT TEST")
    print("initial")
    print_tree_as_list(tree)

    tree.insert(Prefix("00"), 2)
    print("00->2")
    print_tree_as_list(tree)

    tree.insert(Prefix("10"), 2)
    print("10->2")
    print_tree_as_list(tree)

    tree.insert(Prefix("11"), 3)
    print("11->3")
    print_tree_as_list(tree)

    tree.insert(Prefix("010"), 3)
    print("010->3")
    print_tree_as_list(tree)

    tree.insert(Prefix("110"), 4)
    print("110->4")
    print_tree_as_list(tree)


def test_lookup(tree):
    print("LOOKUP TEST")
    print(tree.lookup("255.1.1.1"), 1)
    print(tree.lookup("0.1.1.1"), 2)
    print(tree.lookup("127.1.1.1"), 1)
    print(tree.lookup("64.1.1.1"), 1)
    print(tree.lookup("128.1.1.1"), 2)
    print(tree.lookup("160.1.1.1"), 2)


def test_delete(tree):
    print("DELETE TEST")
    print("initial")
    print_tree_as_list(tree)

    tree.delete(Prefix("00"))
    print("delete 00")
    print_tree_as_list(tree)


def test_print(tree):
    print("PRINT TEST")
    print("initial")
    print_tree_as_list(tree)
    tree.print()
#
# tree = Binary2Tree(1)
# test_insert(tree)
# test_lookup(tree)
# test_delete(tree)
# test_print(tree)

tree = BinaryTree(1)
test_insert(tree)
# test_lookup(tree)
# test_delete(tree)
# test_print(tree)

print_tree(tree)
