from proj1.binary_tree.binarytree import BinaryTree
from proj1.ip_address import to_binary
from proj1.node import Node
import proj1.ip_address as ip
from proj1.prefix import Prefix


class Binary2Tree:

    def __init__(self, default_next_hop):
        # start with only one node with the default next-hop
        self.root = Node(default_next_hop)
        # must store the default next-hop to use in the delete function
        self.default_next_hop = default_next_hop

    def from_file(self, path):
        with open(path) as file:
            for line in file:
                words = line.split()
                if words[0] is '*':
                    self.root.next_hop = words[1]
                else:
                    self.insert(Prefix(words[0]), words[1])

    @staticmethod
    def from_binary_tree(binary_tree):
        """
        :type binary_tree: BinaryTree
        """
        b2tree = Binary2Tree(binary_tree.root.next_hop)
        # the default next-hop of the binary tree is the next-hop of the root node
        b2tree.root = binary_tree.root.copy()
        b2tree.root.clear_next_hop()

        # handle the left side of the tree
        Binary2Tree.__from_binary_tree(binary_tree.root.left, b2tree.root, b2tree.default_next_hop, True)
        # handle the right side of the tree
        Binary2Tree.__from_binary_tree(binary_tree.root.right, b2tree.root, b2tree.default_next_hop, False)
        
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
    def __from_binary_tree(binary_cur_node, binary2_cur_node, next_hop, left):
        """
        :type binary_cur_node: Node
        :type binary2_cur_node: Node
        :type next_hop: int
        :type left: bool
        """
        if binary_cur_node is None:
            # reached a leaf in the tree
            # set the binary 2-tree current node next-hop
            binary2_cur_node.next_hop = next_hop

        else:
            # move binary2 current node to the new node
            new_node = binary_cur_node.copy()
            # set the new node as blank in the binary 2-tree
            new_node.clear_next_hop()

            if binary2_cur_node:

                if left:
                    # new node is the left child of the binary2_cur_node
                    binary2_cur_node.left = new_node
                else:
                    # new node is the right child of the binary2_cur_node
                    binary2_cur_node.right = new_node

                # store a new next-hop if the current node in the binary tree is not blank
                if binary_cur_node.next_hop:
                    next_hop = binary_cur_node.next_hop

            # create new nodes if the current node of the normal binary tree has exactly one child
            if binary_cur_node.left and not binary_cur_node.right:
                # create right node
                new_node.right = Node(next_hop)
                # move to left node
                Binary2Tree.__from_binary_tree(binary_cur_node.left, new_node, next_hop, True)

            elif binary_cur_node.right and not binary_cur_node.left:
                # create left node
                new_node.left = Node(next_hop)
                # move to right node
                Binary2Tree.__from_binary_tree(binary_cur_node.right, new_node, next_hop, False)
            else:
                # move to left node
                Binary2Tree.__from_binary_tree(binary_cur_node.left, new_node, next_hop, True)
                # move to right node
                Binary2Tree.__from_binary_tree(binary_cur_node.right, new_node, next_hop, False)

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
