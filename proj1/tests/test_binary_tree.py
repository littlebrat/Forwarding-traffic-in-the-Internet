from proj1.binary_2tree.binary_2tree import Binary2Tree
from proj1.binary_tree.binarytree import BinaryTree
from proj1.prefix import Prefix


def print_tree(tree):
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
    print_tree(tree)

    tree.insert(Prefix("00"), 2)
    print("00->2")
    print_tree(tree)

    tree.insert(Prefix("10"), 2)
    print("10->2")
    print_tree(tree)

    tree.insert(Prefix("0001"), 3)
    print("0001->3")
    print_tree(tree)

    tree.insert(Prefix("0101"), 2)
    print("0101->2")
    print_tree(tree)

    tree.insert(Prefix("0001"), 4)
    print("0001->4")
    print_tree(tree)


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
    print_tree(tree)

    tree.delete(Prefix("00"))
    print("delete 00")
    print_tree(tree)


def test_print(tree):
    print("PRINT TEST")
    print("initial")
    print_tree(tree)
    tree.print()

tree = Binary2Tree(1)
test_insert(tree)
test_lookup(tree)
test_delete(tree)
test_print(tree)

tree = BinaryTree(1)
test_insert(tree)
test_lookup(tree)
test_delete(tree)
test_print(tree)