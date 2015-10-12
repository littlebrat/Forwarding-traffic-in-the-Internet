from proj1.binary_tree.binarytree import BinaryTree
from proj1.ip_address import quad_doted_to_binary


def files_test():
    tree_array = []
    for i in range(10):
        print('>>> test: ' + str(i)+'\n')
        tree = BinaryTree()
        tree.from_file('../test_files/test_'+str(i)+'.txt')
        tree_array.append(tree)
        tree.print()
        print()
    return tree_array


def files_lookup(trees):
    i = 0
    for t in trees:
        print('>>> test: ' + str(i)+'\n')
        i += 1
        print(t.lookup("255.22.0.69"), quad_doted_to_binary("255.22.0.69"))
        print(t.lookup("0.42.1.1"), quad_doted_to_binary("0.42.1.1"))
        print(t.lookup("127.10.100.0"), quad_doted_to_binary("127.10.100.0"))
        print(t.lookup("64.27.88.88"), quad_doted_to_binary("64.27.88.88"))
        print(t.lookup("27.0.90.22"), quad_doted_to_binary("27.0.90.22"))
        print(t.lookup("160.70.34.56"), quad_doted_to_binary("160.70.34.56"))
        print()

trees = files_test()
files_lookup(trees)
