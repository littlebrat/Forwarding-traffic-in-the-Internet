from proj1.prefix import Prefix
import proj1.tests.trees as trees

btree = trees.build_tree1()

btree.print()
print()
btree.delete(Prefix(''))
btree.print()
