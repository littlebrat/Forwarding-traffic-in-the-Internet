import proj1.tests.test_utils as utils

tree = utils.build_prof_tree()

print("INITIAL TREE")
utils.print_tree(tree)

# compress test
tree.compress()
print("COMPRESSED")
utils.print_tree(tree)
