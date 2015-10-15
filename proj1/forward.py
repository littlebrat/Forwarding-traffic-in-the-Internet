import sys

from proj1.binarytree import BinaryTree
from proj1.binary_2tree import Binary2Tree
from proj1.prefix import Prefix


def helpmsg():
    print('\n AddPrefix (-b) [x] [p] [n] \t  usage: adds the prefix [p] to the corresponding tree [x] with the chosen next hop value [n].')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\t [p]: choose the binary prefix added to the tree [x].')
    print('\t [n]: choose the next hop value for this prefix [p]')
    print('\n DeletePrefix (-b | -q) [x] [p] \t usage: delete the prefix [p] from the tree [x]')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\t [p]: choose the binary prefix added to the tree [x].')
    print('\n PrintTable [x] \t usage: prints the table from the corresponding tree.')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\n AddressLookUp [x] [ip] \t usage: look up the corresponding next hop value on the tree [x] assigned to the address [ip]')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\t [ip]: choose the wanted ip to track the next hop')
    print('\n ReadTable [x] [path] \t usage: read the the table file [path] and build the corresponding tree [x]')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\t [path]: the relative path to this file execution.')
    print('\n Print [x] \t usage: prints graphically the tree [x] to the terminal output.')
    print('\t [x]: choose 1 if relative to binary tree and 2 if relative to the 2-tree.')
    print('\n TwoTree \t usage: convert the binary tree to a 2-tree.')
    print('\n exit \t usage: quit the application.')


def main(path=None):
    print('Forwarding data-packets in a router, using binary trees and 2-trees for representing forwarding tables.')
    print('Type -h or help for instructions on program routines.')

    bin_tree = None

    if len(path) == 2:
        try:
            bin_tree = BinaryTree.from_file(path[1])
        except FileNotFoundError:
            print("the given file doesn't exist")

    while True:

        x = input()
        args = x.split(' ')

        try:
            if args[0] == 'exit':
                sys.exit()

            elif args[0] == 'ReadTable':
                try:
                    bin_tree = BinaryTree.from_file(args[1])
                except FileNotFoundError:
                    print("the given file doesn't exist")

            else:
                if not bin_tree:
                    print("Binary tree is not set yet")
                    print("Use the 'ReadTable' command to initialize the binary tree")
                    continue

                if args[0] == 'PrintTable':
                    bin_tree.print_table()

                elif args[0] == 'AddPrefix':
                    try:
                        if args[1] == '*':
                            bin_tree.insert(Prefix('', '-b'), args[2])
                        elif args[1] == '-b':
                            bin_tree.insert(Prefix(args[2], '-b'), args[3])
                        else:
                            bin_tree.insert(Prefix(args[1], '-q'), args[2])

                    except Exception:
                        print("Prefix format is not correct. Two formats are supported:")
                        print("\t-q Quad-doted, ex: 1.2.3.0/24")
                        print("\t-b Binary, ex:101010101010")

                elif args[0] == 'AddressLookUp':
                    print(bin_tree.lookup(args[1]))

                elif args[0] == 'DeletePrefix':
                    try:
                        if args[1] == '*':
                            bin_tree.delete(Prefix('', '-b'))
                        elif args[1] == '-b':
                            bin_tree.delete(Prefix(args[2], '-b'))
                        else:
                            bin_tree.delete(Prefix(args[1], '-q'))

                    except Exception:
                        print("Prefix format is not correct. Two formats are supported:")
                        print("\t-q Quad-doted, ex: 1.2.3.0/24")
                        print("\t-b Binary, ex:101010101010")

                    bin_tree.delete(Prefix(args[1]))

                elif args[0] == 'Print':
                    bin_tree.print()

                elif args[0] == 'help' or args[0] == '-h':
                    helpmsg()

                else:
                    print("Given command is not valid please read the help instructions")
                    helpmsg()

        except IndexError:
            print("Given command is not valid please read the help instructions")
            helpmsg()

if __name__ == "__main__":
    main(sys.argv)
