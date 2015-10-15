from proj1.binary_tree.binarytree import BinaryTree
from proj1.prefix import Prefix


def build_tree1() -> BinaryTree:
    tree = BinaryTree(1)
    tree.insert(Prefix('00'), 2)
    tree.insert(Prefix('01'), 3)
    return tree
