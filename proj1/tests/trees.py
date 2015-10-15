from proj1.binarytree import BinaryTree
from proj1.prefix import Prefix


def build_tree1() -> BinaryTree:
    """
    It builds the following tree:
    (0, 1)
                (3, 3)
        (1, )
                (2, 2)
    """
    tree = BinaryTree(1)
    tree.insert(Prefix('00'), 2)
    tree.insert(Prefix('01'), 3)
    return tree


def build_tree2():
    """
    It builds the following tree:
                        (5, 3)
                            (8, 4)
            (3, )
                    (4, 2)
    (0, 1)
                    (6, )
                            (7, 3)
            (1, )
                    (2, 2)
    """
    tree = BinaryTree(1)
    tree.insert(Prefix('00'), 2)
    tree.insert(Prefix('10'), 2)
    tree.insert(Prefix('11'), 3)
    tree.insert(Prefix('010'), 3)
    tree.insert(Prefix('110'), 4)
    return tree
