from proj1.binary_tree.binarytree import BinaryTree
from proj1.prefix import Prefix

btree = BinaryTree(1)
btree.insert(Prefix('111'), 3)
btree.insert(Prefix('11011'), 2)

print("Initial tree")
btree.print()
print()

print("Tree after compress insert")
btree.insert_compress(Prefix('110'), 3)
btree.print()
print()

