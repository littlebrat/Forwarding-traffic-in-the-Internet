from proj1.binarytree import BinaryTree
from proj1.ip_address import to_binary
from proj1.node import Node
import proj1.ip_address as ip


class Binary2Tree:

    def __init__(self, binary_tree: BinaryTree):
        self.root = Binary2Tree.__from_binary_tree(binary_tree.root)
        
    def lookup(self, ip_address, format=ip.Format.quad_doted):
        # convert ip address to binary format
        binary_address = to_binary(ip_address, format)

        # start with no next-hop
        next_hop = None
        # start at the tree root
        cur_node = self.root
        for bit in binary_address:

            if cur_node is None:
                # reach the leaf of the tree
                # lookup is done
                break

            # store a new next hop only
            next_hop = cur_node.next_hop if cur_node.next_hop else next_hop

            if bit is '1':
                # move right
                cur_node = cur_node.right
            else:
                # move left
                cur_node = cur_node.left

        return next_hop

    def print(self):
        Binary2Tree.__print_node(self.root, 0)

    def print_table(self):
        Binary2Tree.__print_table_node(self.root, '')

    @staticmethod
    def __from_binary_tree(bnode: Node, b2node: Node=None, inherited_nexthop=None, left=None):

        if not bnode:
            # reached a leaf in the binary 2-tree
            b2node.next_hop = inherited_nexthop
            return b2node

        # store the inherited next-hop
        if bnode.next_hop is not None:
            inherited_nexthop = bnode.next_hop

        # create the new node blank to insert in the binary 2-tree
        new_node = bnode.copy()
        new_node.clear_next_hop()

        if not b2node:
            # this is the root of the binary 2-tree
            b2node = new_node
        else:
            # add the new node to the binary 2-tree and move to the new node
            if left:
                b2node.left = new_node
                b2node = b2node.left
            else:
                b2node.right = new_node
                b2node = b2node.right

        # move to the next child and create any missing child in the binary 2 tree
        if bnode.left and not bnode.right:
            # the binary node has only the left child
            # create the right child in the binary 2-tree
            b2node.right = Node(inherited_nexthop)

            # move to the left child in the binary tree
            Binary2Tree.__from_binary_tree(bnode.left, b2node, inherited_nexthop, True)

        elif not bnode.left and bnode.right:
            # the binary node has only the right child
            # create the left child in the binary 2-tree
            b2node.left = Node(inherited_nexthop)

            # move to the right child in the binary tree
            Binary2Tree.__from_binary_tree(bnode.right, b2node, inherited_nexthop, False)

        else:
            # the binary tree node has both children
            # move to both children
            Binary2Tree.__from_binary_tree(bnode.left, b2node, inherited_nexthop, True)
            Binary2Tree.__from_binary_tree(bnode.right, b2node, inherited_nexthop, False)

        return b2node

    @staticmethod
    def __print_table_node(node, bits):
        if node is not None:
            if node.next_hop:
                print(bits, node.next_hop)

            # print left node
            Binary2Tree.__print_table_node(node.left, bits + '0')

            # print right node
            Binary2Tree.__print_table_node(node.right, bits + '1')

    @staticmethod
    def __print_node(node, level):
        if node:

            # print right node
            Binary2Tree.__print_node(node.right, level + 1)

            # print the same number of tabs as the level of the node
            for i in range(0, 2*level):
                print('\t', end='')

            # print the node next-hop
            print(node)

            # print left node
            Binary2Tree.__print_node(node.left, level + 1)
