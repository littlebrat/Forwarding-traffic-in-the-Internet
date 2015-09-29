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


def _inherited(node, parents):
    if node.next_hop():
        return node.next_hop()
    else:
        # the list of parents of the parent(node) is the list of parent nodes without the
        # first parent node in the list
        # inherited(parent(node), parents of parent(node))
        return _inherited(parents[0], parents[1:]) if len(parents) > 0 else None


def _print_table_node(node, bits):
    if node is not None:
        if node.next_hop():
            print(bits, node.next_hop())

        # print left node
        _print_table_node(node.left(), bits + '0')

        # print right node
        _print_table_node(node.right(), bits + '1')


def _print_node(node, level):
    if node:

        # print right node
        _print_node(node.right(), level + 1)

        # print the same number of tabs as the level of the node
        for i in range(0, 2*level):
            print('\t', end='')

        # print the node next-hop
        print(node)

        # print left node
        _print_node(node.left(), level + 1)


class BinaryTree:

    def __init__(self, default_next_hop):
        # start with only one node with the default next-hop
        self.root = Node(default_next_hop)

    def insert(self, prefix, next_hop):
        cur_node = self.root
        for bit in prefix:
            if bit is 1:
                # move to the right
                if cur_node.right() is None:
                    # create node if necessary
                    cur_node.set_right(Node())
                # move the current node to the right node
                cur_node = cur_node.right()
            else:
                # move to the left
                if cur_node.left() is None:
                    # create node if necessary
                    cur_node.set_left(Node())
                # move the current node to the left node
                cur_node = cur_node.left()
        # set the next-hop of the final node
        cur_node.set_next_hop(next_hop)

    def lookup(self, ip_address, format=ip.Format.quad_doted):
        # convert ip address to binary format
        binary_address = _to_binary(ip_address, format)

        # starting point for the search
        cur_node = self.root
        hop = cur_node.next_hop()
        for bit in binary_address:
            if bit is '1':
                # memorize the hop if it is valid
                if cur_node.next_hop():
                    hop = cur_node.next_hop()
                # move to the right
                if cur_node.right() is None:
                    # if there is not any node right, longest prefix has been found
                    return hop
                    # return the nextHop for this ip
                # move right
                cur_node = cur_node.right()
            else:
                # memorize the hop if it is valid
                if cur_node.next_hop():
                    hop = cur_node.next_hop()
                # move to the left
                if cur_node.left() is None:
                    # if there is not any node left, longest prefix has been found
                    return hop
                    # return the nextHop for this ip
                # move left
                cur_node = cur_node.left()

    def delete(self, prefix):
        cur_node = self.root
        # reference to delete
        parent, side = cur_node, ''
        for bit in prefix:
            if bit is 1:
                # find if the current node has 2 children
                if cur_node.right() is not None and cur_node.left() is not None:
                    parent, side = cur_node, 1
                # move to the right
                cur_node = cur_node.right()
            else:
                # find if the current node has 2 children
                if cur_node.right() is not None and cur_node.left() is not None:
                    parent, side = cur_node, 0
                # move to the left
                cur_node = cur_node.left()
        if cur_node.right() is not None or cur_node.left() is not None:
            cur_node.unset_next_hop()
        else:
            if side is 1:
                # delete the right child of the tree
                parent.set_right(None)
            elif side is 0:
                # delete the left child of the tree
                parent.set_left(None)

    # for each node N (root to leaves) {
    #     if N has exactly one child node,
    #         create the missing child node
    #     if nexthops(N) = ∅,
    #         nexthops(N) ← inherited(N)
    # }
    def _to_Binary2Tree(self, cur_node, parents, inherited_next_hop):

        if cur_node:
            # create missing child if the current node has exactly one child
            if cur_node.left() and not cur_node.right():
                # create the left child
                cur_node.set_left(Node())
            elif cur_node.right() and not cur_node.left():
                # create the right i
                cur_node.set_right(Node())

            if not cur_node.next_hop():
                cur_node.set_next_hop(inherited_next_hop)
            else:
                inherited_next_hop = cur_node.next_hop()

            # add current node to the lis tof parents
            parents = [cur_node] + parents[:]

            # move to the left node
            self._to_Binary2Tree(cur_node.left(), parents, inherited_next_hop)
            # move to the right node
            self._to_Binary2Tree(cur_node.right(), parents, inherited_next_hop)

    def to_Binary2Tree(self):
        self._to_Binary2Tree(self.root, [], None)
        return self

    def print_table(self):
        _print_table_node(self.root, '')

    def print(self):
        _print_node(self.root, 0)

