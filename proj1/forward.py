import sys
from proj1.binary_tree.binarytree import BinaryTree
from proj1.binary_2tree.binary_2tree import Binary2Tree
from proj1.prefix import Prefix


def main(path = None):
    print('Forwarding data-packets in a router, using binary trees and 2-trees for representing forwarding tables.')
    file_name = path
    bin_tree = BinaryTree()
    bin_2tree = Binary2Tree(1)
    if path != None:
        bin_tree.from_file(path)
    while True:
        x = input()
        args = x.split(' ')
        if args[0] == 'exit' and len(args) == 1:
            sys.exit()
        elif args[0] == 'PrintTable' and len(args) == 2:
            if args[1] == '1':
                bin_tree.print_table()
            elif args[1] == '2':
                bin_2tree.print_table()
            else:
                print('wrong command format')
        elif args[0] == 'TwoTree' and len(args) == 1:
            bin_2tree.from_binary_tree(bin_tree)
        elif args[0] == 'AddPrefix' and len(args) == 4:
            if args[1] == '1':
                bin_tree.insert(Prefix(args[2]),args[3])
            elif args[1] == '2':
                bin_2tree.insert(Prefix(args[2]),args[3])
            else:
                print('wrong command format')
        elif args[0] == 'AddressLookUp' and len(args) == 3:
            if args[1] == '1':
                bin_tree.lookup(args[2])
            elif args[1] == '2':
                bin_2tree.lookup(args[2])
            else:
                print('wrong command format')
        elif args[0] == 'DeletePrefix' and len(args) == 3:
            if args[1] == '1':
                bin_tree.delete(Prefix(args[2]))
            elif args[1] == '2':
                bin_2tree.delete(Prefix(args[2]))
            else:
                print('wrong command format')
        elif args[0] == 'ReadTable' and len(args) == 3:
            file_name = args[2]
            if args[1] == '1':
                bin_tree = BinaryTree()
                bin_tree.from_file(file_name)
            elif args[1] == '2':
                bin_2tree = Binary2Tree(1)
                bin_2tree.from_file(file_name)
            else:
                print('wrong command format')
        else:
            print('wrong command format')

if __name__ == "__main__":
    main(sys.argv[1])