from proj1.binarytree import BinaryTree
from proj1.prefix import Prefix
import proj1.tests.trees as trees

btree = trees.build_tree1()

btree.print()
print()
btree.delete(Prefix(''))
btree.print()
print()

print("file test_1.txt")
btree = BinaryTree.from_file('/home/david/Development/IST/ADRC/Mini-Projecto-1/proj1/test_files/test_1.txt')
btree.print()
print()

btree.delete(Prefix('001'))
btree.delete(Prefix('01'))
btree.delete(Prefix('10'))
btree.delete(Prefix('11'))

btree.print()
print()
btree.delete(Prefix('000'))
btree.print()
print()