from binarytree import BinaryTree
from prefix import Prefix

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

tree = BinaryTree(1)
tree.insert_compress(Prefix('00'), 2)
tree.insert_compress(Prefix('10'), 2)
tree.insert_compress(Prefix('11'), 3)

print("COMPRESSED")
tree.print()

