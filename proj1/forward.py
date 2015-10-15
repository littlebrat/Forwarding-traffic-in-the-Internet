import sys
from proj1.binary_tree.binarytree import BinaryTree
from proj1.binary_2tree.binary_2tree import Binary2Tree
from proj1.prefix import Prefix


def helpmsg():
    print('\n AddPrefix [p] [n] \t  usage: adds the prefix [p] to the binary tree with the chosen next hop value [n].')
    print('\t [p]: choose the binary prefix added to the tree [x].')
    print('\t [n]: choose the next hop value for this prefix [p].')
    print('\n DeletePrefix [p] \t usage: delete the prefix [p] from the binary tree.')
    print('\t [p]: choose the binary prefix deleted from the tree.')
    print('\n PrintTable [x] \t usage: prints the table from the corresponding tree.')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\n AddressLookUp [x] [ip] \t usage: look up the corresponding next hop value on the tree [x] assigned to the address [ip].')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\t [ip]: choose the wanted ip to track the next hop.')
    print('\n ReadTable [path] \t usage: read the the table file [path] and build the corresponding binary tree.')
    print('\t [path]: the relative path to this file execution.')
    print('\n Print [x] \t usage: prints graphically the tree [x] to the terminal output.')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\n TwoTree \t usage: convert the binary tree to a 2-tree.')
    print('\n exit \t usage: quit the application.')


def main(path = None):
    print('Forwarding data-packets in a router, using binary trees and 2-trees for representing forwarding tables.')
    print('Type -h or help for instructions on program routines.')

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
                print('Type -h or help for instructions on program routines.')
        elif args[0] == 'TwoTree' and len(args) == 1:
            bin_2tree = Binary2Tree.from_binary_tree(bin_tree)
        elif args[0] == 'AddPrefix' and len(args) == 4:
            if args[1] == '1':
                bin_tree.insert(Prefix(args[2]), args[3])
            elif args[1] == '2':
                bin_2tree.insert(Prefix(args[2]), args[3])
            else:
                print('wrong command format')
                print('Type -h or help for instructions on program routines.')
        elif args[0] == 'AddressLookUp' and len(args) == 3:
            if args[1] == '1':
                bin_tree.lookup(args[2])
            elif args[1] == '2':
                bin_2tree.lookup(args[2])
            else:
                print('wrong command format')
                print('Type -h or help for instructions on program routines.')
        elif args[0] == 'DeletePrefix' and len(args) == 3:
            if args[1] == '1':
                bin_tree.delete(Prefix(args[2]))
            elif args[1] == '2':
                bin_2tree.delete(Prefix(args[2]))
            else:
                print('wrong command format')
                print('Type -h or help for instructions on program routines.')
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
                print('Type -h or help for instructions on program routines.')
        elif args[0] == 'Print' and len(args) == 2:
            if args[1] == '1':
                bin_tree.print()
            elif args[1] == '2':
                bin_2tree.print()
        elif args[0] == 'help' or args[0] == '-h' and len(args) == 1:
            helpmsg()
        else:
            print('wrong command format')
            print('Type -h or help for instructions on program routines.')

if __name__ == "__main__":
    main(sys.argv[1])
