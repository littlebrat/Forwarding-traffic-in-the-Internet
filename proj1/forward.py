import sys

from binarytree import BinaryTree
from binary_2tree import Binary2Tree
from prefix import Prefix


def helpmsg():
    print()
    print('AddPrefix (-b) [p] [n]   adds the prefix [p] to the current table with the next-hop value [n]')
    print('DeletePrefix (-b) [p]    deletes the prefix [p] from the binary tree.')
    print('PrintTable               prints current table')
    print('AddressLookUp [ip]       looks up the next-hop for the given ip address [ip]')
    print('ReadTable [path]         builds the binary tree from the given file')
    print('PrintTree                prints the table in a tree format')
    print('exit                     quits the application')


def main(path=None):
    print('Forwarding data-packets in a router, using binary trees and 2-trees for representing forwarding tables.')
    print('Type -h or help for instructions on program routines.')

    bin_tree = None
    bin2_tree = None

    if len(path) == 2:
        try:
            bin_tree = BinaryTree.from_file(path[1])
            bin2_tree = Binary2Tree(bin_tree)
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
                    bin2_tree = Binary2Tree(bin_tree)
                except FileNotFoundError:
                    print("the given file doesn't exist")

            elif args[0] == 'help' or args[0] == '-h':
                    helpmsg()

            else:
                if not bin_tree:
                    print("Binary tree is not set yet")
                    print("Use the 'ReadTable' command to initialize the binary tree")
                    continue

                if args[0] == 'PrintTable':
                    print("Binary Tree")
                    bin_tree.print_table()
                    print()
                    print("Binary 2-tree")
                    bin2_tree.print_table()
                    print()

                elif args[0] == 'AddPrefix':
                    try:
                        if args[1] == '*':
                            bin_tree.insert(Prefix('', '-b'), args[2])
                        elif args[1] == '-b':
                            bin_tree.insert(Prefix(args[2], '-b'), args[3])
                        else:
                            bin_tree.insert(Prefix(args[1], '-q'), args[2])

                        bin2_tree = Binary2Tree(bin_tree)

                    except Exception:
                        print("Prefix format is not correct. Two formats are supported:")
                        print("\tQuad-doted, ex: 1.2.3.0/24")
                        print("\tBinary, ex:101010101010")

                elif args[0] == 'AddressLookUp':
                    print("Lookup on the binary tree: ", bin_tree.lookup(args[1]))
                    print("Lookup on the binary 2-tree: ", bin2_tree.lookup(args[1]))

                elif args[0] == 'DeletePrefix':
                    try:
                        if args[1] == '*':
                            bin_tree.delete(Prefix('', '-b'))
                        elif args[1] == '-b':
                            bin_tree.delete(Prefix(args[2], '-b'))
                        else:
                            bin_tree.delete(Prefix(args[1], '-q'))

                        bin2_tree = Binary2Tree(bin_tree)

                    except Exception:
                        print("Prefix format is not correct. Two formats are supported:")
                        print("\tQuad-doted, ex: 1.2.3.0/24")
                        print("\tBinary, ex:101010101010")

                elif args[0] == 'PrintTree':
                    print("Binary Tree")
                    bin_tree.print()
                    print()
                    print("Binary 2-Tree")
                    bin2_tree.print()
                    print()

                else:
                    print("Given command is not valid please read the help instructions")
                    helpmsg()

        except IndexError:
            print("Given command is not valid please read the help instructions")
            helpmsg()

if __name__ == "__main__":
    main(sys.argv)
