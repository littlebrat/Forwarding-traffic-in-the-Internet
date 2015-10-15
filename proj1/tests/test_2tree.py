from proj1.binary_2tree.binary_2tree import Binary2Tree
from proj1.prefix import Prefix
import proj1.tests.trees as trees

btree = trees.build_tree1()

print("Initial tree")
btree.print()
b2tree = Binary2Tree(btree)
b2tree.print()
print()

print("After insert 0/4")
btree.insert(Prefix('0'), 4)
btree.print()
b2tree = Binary2Tree(btree)
b2tree.print()
print()

print("After delete 01/3")
btree.delete(Prefix('01'))
btree.print()
b2tree = Binary2Tree(btree)
b2tree.print()
print()
