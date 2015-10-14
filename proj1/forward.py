import sys
from proj1.binary_tree.binarytree import BinaryTree
from proj1.binary_2tree.binary_2tree import Binary2Tree


def main():
    print('Forwarding data-packets in a router, using binary trees and 2-trees for representing forwarding tables.')

    with_arg_user_cmds = {
        'ReadTable': 'from_file', 'AddPrefix': 'insert', 'DeletePrefix': 'delete',
        'AddressLookUp': 'lookup'
    }
    no_arg_user_cmds = {
        'PrintTable': 'print_table', 'TwoTree': 'from_binary_tree', 'exit': 'sys.exit'
    }

    file_name = ''
    bin_tree = BinaryTree()
    #bin_2tree = Binary2Tree()

    x = None
    while True:
        try:
            x = input()
            if len(x.split(' ')) is 1:
                arg1 = x
                if arg1 in no_arg_user_cmds.keys():
                    print('No args!')
                else:
                    raise Exception
            elif len(x.split(' ')) is 2:
                arg1, arg2 = x.split(' ')
                if arg1 in with_arg_user_cmds.keys():
                    print('With args!')
                else:
                    raise Exception
            else:
                raise Exception
        except Exception:
            print('UNKNOWN INPUT FORMAT DETECTED')

if __name__ == "__main__":
    main()
