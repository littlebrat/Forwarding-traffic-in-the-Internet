import tests.test_utils as utils
from binarytree import BinaryTree
from prefix import Prefix


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
