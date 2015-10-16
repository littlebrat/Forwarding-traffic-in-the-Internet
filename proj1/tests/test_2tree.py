from binary_2tree import Binary2Tree
from prefix import Prefix
import tests.trees as trees

btree = trees.build_tree1()

print("Initial tree")
btree.print()
b2tree = Binary2Tree(btree)
print()
b2tree.print()
print()

print("After insert 0/4")
btree.insert(Prefix('0'), 4)
btree.print()
b2tree = Binary2Tree(btree)
print()
b2tree.print()
print()

btree.print_table()

print("After delete 01/3")
btree.delete(Prefix('01'))
btree.print()
b2tree = Binary2Tree(btree)
print()
b2tree.print()
print()

btree.print_table()
