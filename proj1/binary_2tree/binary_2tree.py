from proj1.binary_tree.binarytree import BinaryTree
from proj1.binary_tree.binarytree import _to_binary
from proj1.node import Node
import proj1.ip_address as ip


def _remove_node(parent_node, node, default_next_hop):
    if parent_node is not None:
        if parent_node.left() == node:
            # node is the left node of the parent
            parent_node.left().set_next_hop(default_next_hop)
        elif parent_node.right() == node:
            # node is the right node of the parent
            parent_node.right().set_next_hop(default_next_hop)


def _from_binary_tree(binary_cur_node, binary2_cur_node, next_hop, left):
        """
        :type binary_cur_node: Node
        :type binary2_cur_node: Node
        :type next_hop: int
        :type left: bool
        """
        if binary_cur_node is None:
            # reached a leaf in the tree
            # set the binary 2-tree current node next-hop
            binary2_cur_node.set_next_hop(next_hop)
        else:
            # move binary2 current node to the new node
            new_node = binary_cur_node.copy()
            # set the new node as blank in the binary 2-tree
            new_node.unset_next_hop()

            if binary2_cur_node:

                if left:
                    # new node is the left child of the binary2_cur_node
                    binary2_cur_node.set_left(new_node)
                else:
                    # new node is the right child of the binary2_cur_node
                    binary2_cur_node.set_right(new_node)

                # store a new next-hop if the current node in the binary tree is not blank
                if binary_cur_node.next_hop():
                    next_hop = binary_cur_node.next_hop()

            # move left
            _from_binary_tree(binary_cur_node.left(), new_node, next_hop, True)
            # move right
            _from_binary_tree(binary_cur_node.right(), new_node, next_hop, False)


class Binary2Tree(BinaryTree):
    def __init__(self, default_next_hop):
        super().__init__(default_next_hop)

        # must store the default next-hop to use in the delete function
        self.default_next_hop = default_next_hop

    def from_binary_tree(self, binary_tree):
        """
        :type binary_tree: BinaryTree
        """

        # the default next-hop of the binary tree is the next-hop of the root node
        self.default_next_hop = binary_tree.root.next_hop()
        self.root = binary_tree.root.copy()

        # handle the left side of the tree
        _from_binary_tree(binary_tree.root.left(), self.root, self.default_next_hop, True)
        # handle the right side of the tree
        _from_binary_tree(binary_tree.root.right(), self.root, self.default_next_hop, False)
        
    def insert(self, prefix, next_hop):

        last_next_hop = None
        cur_node = self.root
        for bit in prefix:

            if cur_node.next_hop():
                # store next-hop of the last node with next-hop found
                last_next_hop = cur_node.next_hop()
                # clear node next-hop
                cur_node.unset_next_hop()

            if bit is 1:
                # is to move to the right

                # create node if necessary
                if cur_node.right() is None:
                    cur_node.set_right(Node())

                # check the other side of the node
                # create node if necessary
                if cur_node.left() is None:
                    # create node with the last next-hop of previous node
                    cur_node.set_left(Node(last_next_hop))

                # move the current node to the right node
                cur_node = cur_node.right()

            else:
                # is to move to the left

                # create node if necessary
                if cur_node.left() is None:
                    cur_node.set_left(Node())

                # check the other side of the node
                # create node if necessary
                if cur_node.right() is None:
                    # create node with the last next-hop of previous node
                    cur_node.set_right(Node(last_next_hop))

                # move the current node to the left node
                cur_node = cur_node.left()

        # set the next-hop of the final node
        cur_node.set_next_hop(next_hop)

    def delete(self, prefix):

        # look for the prefix in the tree
        # start looking for the prefix at the root of the tree
        cur_node = self.root

        # list all the visited node in order (from the first to the last)
        visited_nodes = []

        for bit in prefix:

            # add the node to the visited list
            visited_nodes.insert(0, cur_node)

            if cur_node is None:
                # didn't find the prefix
                break

            if bit is 1:
                # move to the right
                cur_node = cur_node.right()
            else:
                # move to the left
                cur_node = cur_node.left()

        if cur_node is not None and cur_node.next_hop():
            # the prefix was found
            # remove node from the tree
            parent_node = visited_nodes[0]
            _remove_node(parent_node, cur_node, self.default_next_hop)

            # remove all the unnecessary nodes
            for node in visited_nodes:

                if not node.left() or not node.right():
                    # reached root node -> can not remove root node
                    break

                # check if both children are equal
                if node.left().next_hop() == node.right().next_hop():
                    # move the next-hop one node up
                    node.set_next_hop(node.left().next_hop())
                    node.set_left(None)
                    node.set_right(None)
                else:
                    # can't move up mode nodes
                    break

    def lookup(self, ip_address, format=ip.Format.quad_doted):
        # convert ip address to binary format
        binary_address = _to_binary(ip_address, format)

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
            next_hop = cur_node.next_hop() if cur_node.next_hop() else next_hop

            if bit is '1':
                # move right
                cur_node = cur_node.right()
            else:
                # move left
                cur_node = cur_node.left()

        return next_hop
