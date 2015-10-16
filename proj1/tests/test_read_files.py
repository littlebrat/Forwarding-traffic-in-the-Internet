from binarytree import BinaryTree
from ip_address import quad_doted_to_binary
from prefix import Prefix


def files_test(debug=False):
    tree_array = []
    for i in range(10):
        if debug is True:
            print('>>> test: ' + str(i)+'\n')
        tree = BinaryTree.from_file('../test_files/test_'+str(i)+'.txt')
        tree_array.append(tree)
        if debug is True:
            tree.print()
            print()
    return tree_array


def files_lookup(trees):
    i = 0
    for t in trees:
        print('>>> test: ' + str(i)+'\n')
        i += 1
        t.print()
        print(t.lookup("255.22.0.69"), quad_doted_to_binary("255.22.0.69"))
        print(t.lookup("0.42.1.1"), quad_doted_to_binary("0.42.1.1"))
        print(t.lookup("127.10.100.0"), quad_doted_to_binary("127.10.100.0"))
        print(t.lookup("64.27.88.88"), quad_doted_to_binary("64.27.88.88"))
        print(t.lookup("27.0.90.22"), quad_doted_to_binary("27.0.90.22"))
        print(t.lookup("160.70.34.56"), quad_doted_to_binary("160.70.34.56"))
        print()

def files_delete_0(trees):
    tree = trees[0]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('00'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('110'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('010'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('10'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('11'))
    tree.print()

def files_delete_1(trees):
    tree = trees[1]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('01'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('10'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('000'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('001'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('11'))
    tree.print()

def files_delete_2(trees):
    tree = trees[2]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('0'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('00'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('000'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('0011'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('00000'))
    tree.print()

def files_delete_3(trees):
    tree = trees[3]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('0'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('00'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('000'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('0011'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('00000'))
    tree.print()

def files_delete_5(trees):
    tree = trees[5]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('00'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('10'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('11'))
    tree.print()

def files_delete_6(trees):
    tree = trees[6]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('000'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('001'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('11'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('10'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('01'))
    tree.print()

def files_delete_7(trees):
    tree = trees[7]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('10101011'))
    tree.print()

def files_delete_8(trees):
    tree = trees[8]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('000'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('100'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('001'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('010'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('111'))
    tree.print()
    print('>>> test: 6\n')
    tree.delete(Prefix('110'))
    tree.print()
    print('>>> test: 7\n')
    tree.delete(Prefix('101'))
    tree.print()
    print('>>> test: 8\n')
    tree.delete(Prefix('011'))
    tree.print()

def files_delete_9(trees):
    tree = trees[9]
    tree.print()
    print('>>> test: 1\n')
    tree.delete(Prefix('0'))
    tree.print()
    print('>>> test: 2\n')
    tree.delete(Prefix('00'))
    tree.print()
    print('>>> test: 3\n')
    tree.delete(Prefix('0000'))
    tree.print()
    print('>>> test: 4\n')
    tree.delete(Prefix('01'))
    tree.print()
    print('>>> test: 5\n')
    tree.delete(Prefix('000'))
    tree.print()


#trees = files_test()
#files_lookup(trees)
#files_delete_0(trees)
#files_delete_1(trees)
#files_delete_2(trees)
#files_delete_3(trees)
#files_delete_4(trees)
#files_delete_5(trees)
#files_delete_6(trees)
#files_delete_7(trees)
#files_delete_8(trees)
#files_delete_9(trees)
