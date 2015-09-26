from proj1.node import Node
import proj1.ip_address as ip


def _to_binary(ip_address, format):
    if format is ip.Format.quad_doted:
        binary_address = ip.quad_doted_to_binary(ip_address)
    elif format is ip.Format.decimal:
        binary_address = ip.decimal_to_binary(ip_address)
    elif format is ip.Format.binary:
        binary_address = ip_address
    else:
        raise Exception("invalid ip address format")

    return binary_address

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

    def lookup(self, ip_address, format=ip.Format.quad_doted):
        # convert ip address to binary format
        binary_address = _to_binary(ip_address, format)

        # start with no next-hop
        next_hop = -1
        # start at the tree root
        cur_node = self.root
        for bit in binary_address:

            if cur_node is None:
                # reach the leaf of the tree
                # lookup is done
                break

            # store a new next hop only
            next_hop = cur_node.next_hop() if cur_node.next_hop() != -1 else next_hop

            if bit is '1':
                # move right
                cur_node = cur_node.right()
            else:
                # move left
                cur_node = cur_node.left()

        return next_hop
