import proj1.tests.test_utils as utils
from proj1.binary_tree.binarytree import BinaryTree
from proj1.prefix import Prefix


tree = utils.build_prof_tree()

print("INITIAL TREE")
utils.print_tree(tree)

# compress test
tree.compress()
print("COMPRESSED")
utils.print_tree(tree)

# build the original binary tree of the ORTC paper
tree = BinaryTree(1)
tree.insert(Prefix('00'), 2)
tree.insert(Prefix('10'), 2)
tree.insert(Prefix('11'), 3)

print("INITIAL TREE")
utils.print_tree(tree)

# compress test
tree.compress()
print("COMPRESSED")
utils.print_tree(tree)
