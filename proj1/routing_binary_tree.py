from proj1.prefix import Prefix
from proj1.node import Node

class RoutingBinaryTree:

    def __init__(self, default_next_hop):
        # start with only one node with the default next-hop
        self.root = Node(default_next_hop)

    def insert(self, prefix, next_hop):

        last_next_hop = -1
        cur_node = self.root
        for bit in prefix:

            if cur_node.next_hop() != -1:
                # store next-hop of the last node with next-hop found
                last_next_hop = cur_node.next_hop()
                # clear node next-hop
                cur_node.set_next_hop(-1)

            if bit is 1:
                # is to move to the right

                # create node if necessary
                if cur_node.right() is None:
                    cur_node.set_right(Node(-1))

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
                    cur_node.set_left(Node(-1))

                # check the other side of the node
                # create node if necessary
                if cur_node.right() is None:
                    # create node with the last next-hop of previous node
                    cur_node.set_right(Node(last_next_hop))

                # move the current node to the left node
                cur_node = cur_node.left()

        # set the next-hop of the final node
        cur_node.set_next_hop(next_hop)

    def remove(self, prefix):
        pass

    def lookup(self, prefix):
        pass
