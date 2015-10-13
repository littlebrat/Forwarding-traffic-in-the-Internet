from collections import deque
from proj1.node import Node
from proj1.prefix import Prefix
from proj1.ip_address import to_binary
import proj1.ip_address as ip


class BinaryTree:

    def __init__(self, default_next_hop=None):
        # start with only one node with the default next-hop
        self.root = Node(default_next_hop)

    def from_file(self, path):
        with open(path) as file:
            for line in file:
                words = line.split()
                if words[0] is '*':
                    self.root.next_hop = words[1]
                else:
                    self.insert(Prefix(words[0]), words[1])

    def insert(self, prefix, next_hop):
        cur_node = self.root
        for bit in prefix:
            if bit is 1:
                # move to the right
                if cur_node.right is None:
                    # create node if necessary
                    cur_node.right = Node()
                # move the current node to the right node
                cur_node = cur_node.right
            else:
                # move to the left
                if cur_node.left is None:
                    # create node if necessary
                    cur_node.left = Node()
                # move the current node to the left node
                cur_node = cur_node.left
        # set the next-hop of the final node
        cur_node.next_hop = next_hop

    def insert_compress(self, prefix, next_hop):
        # queue with all the visited nodes
        visited_nodes = deque()

        # 1st step - move in the tree until finding the prefix position and expand the visited nodes
        cur_node = self.root
        cur_next_hop = cur_node.next_hop
        for bit in prefix:
            # update the next hop if the current node has a next hop
            if cur_node.next_hop:
                cur_next_hop = cur_node.next_hop

            BinaryTree.__expand_node(cur_node, cur_next_hop)
            visited_nodes.append(cur_node)

            if bit:
                # ensure the left node has as next-hop a set and not an int
                if cur_node.left.next_hop:
                    cur_node.left.next_hop = {cur_node.left.next_hop}

                # move to the right node and create one if necessary
                if not cur_node.right:
                    cur_node.right = Node()
                cur_node = cur_node.right

                # store the non-visited node to be used in the 3rd and 4th steps
                visited_nodes.append(cur_node.left)

            else:
                # ensure the right node has as next-hop a set and not an int
                if cur_node.right.next_hop:
                    cur_node.right.next_hop = {cur_node.right.next_hop}

                # move to the left node and create one if necessary
                if not cur_node.left:
                    cur_node.left = Node()
                cur_node = cur_node.left

                # store the non-visited node to be used in the 3rd and 4th steps
                visited_nodes.append(cur_node.left)

        # after leaving the loop cur_node points to the node where the prefix is stored
        visited_nodes.append(cur_node)

        # 2nd step - expand the descendants
        # queue used to move in the tree level by level
        node_queue = deque()

        # initialize queue with the first node
        cur_node.next_hop = cur_next_hop = next_hop
        node_queue.appendleft(cur_node)

        while len(node_queue) > 0:
            cur_node = node_queue.pop()
            visited_nodes.append(cur_node)

            if cur_node.next_hop:
                cur_next_hop = cur_node.next_hop

            # expand the node
            if cur_node.left and not cur_node.right:
                cur_node.right = Node({cur_next_hop})
                cur_node.clear_next_hop()

                # add the non created node
                node_queue.appendleft(cur_node.left)
            elif not cur_node.left and cur_node.right:
                cur_node.left = Node({cur_next_hop})
                cur_node.clear_next_hop()

                # add the non created node
                node_queue.appendleft(cur_node.right)
            elif not cur_node.left and not cur_node.right:
                # ensure that when a node is a leaf it's next-hop is a set and not an int
                cur_node.next_hop = {cur_node.next_hop}

    def lookup(self, ip_address, format=ip.Format.quad_doted):
        # convert ip address to binary format
        binary_address = to_binary(ip_address, format)

        # starting point for the search
        cur_node = self.root
        hop = cur_node.next_hop
        for bit in binary_address:
            if bit is '1':
                # memorize the hop if it is valid
                if cur_node.next_hop:
                    hop = cur_node.next_hop
                # move to the right
                if cur_node.right is None:
                    # if there is not any node right, longest prefix has been found
                    return hop
                    # return the nextHop for this ip
                # move right
                cur_node = cur_node.right
            else:
                # memorize the hop if it is valid
                if cur_node.next_hop:
                    hop = cur_node.next_hop
                # move to the left
                if cur_node.left is None:
                    # if there is not any node left, longest prefix has been found
                    return hop
                    # return the nextHop for this ip
                # move left
                cur_node = cur_node.left

    def delete(self, prefix):
        cur_node = self.root
        # reference to delete
        parent, side = cur_node, ''
        for bit in prefix:
            if bit is 1:
                # find if the current node has 2 children
                if cur_node.right is not None and cur_node.left is not None:
                    parent, side = cur_node, 1
                # move to the right
                cur_node = cur_node.right
            else:
                # find if the current node has 2 children
                if cur_node.right is not None and cur_node.left is not None:
                    parent, side = cur_node, 0
                # move to the left
                cur_node = cur_node.left
        if cur_node.right is not None or cur_node.left is not None:
            cur_node.clear_next_hop()
        else:
            if side is 1:
                # delete the right child of the tree
                parent.clear_right()
            elif side is 0:
                # delete the left child of the tree
                parent.clear_left()

    def compress(self):
        # first step
        BinaryTree.__compress_first_step(self.root, None, self.root.next_hop)

        # second step
        BinaryTree.__get_next_hops(self.root)

        # third step
        # set the next-hop of the root as one of next-hops in it's set
        self.root.next_hop = self.root.next_hop.pop()
        # choose the next-hop of the left node
        BinaryTree.__choose_next_hop(self.root.left, self.root, self.root.next_hop, True)
        # choose the next-hop of the right node
        BinaryTree.__choose_next_hop(self.root.right, self.root, self.root.next_hop, False)

    def print(self):
        BinaryTree.__print_node(self.root, 0)

    def print_table(self):
        BinaryTree.__print_table_node(self.root, '')

    @staticmethod
    def __print_table_node(node, bits):
        if node is not None:
            if node.next_hop:
                print(bits, node.next_hop)

            # print left node
            BinaryTree.__print_table_node(node.left, bits + '0')

            # print right node
            BinaryTree.__print_table_node(node.right, bits + '1')

    @staticmethod
    def __print_node(node, level):
        if node:

            # print right node
            BinaryTree.__print_node(node.right, level + 1)

            # print the same number of tabs as the level of the node
            for i in range(0, 2*level):
                print('\t', end='')

            # print the node next-hop
            print(node)

            # print left node
            BinaryTree.__print_node(node.left, level + 1)

    @staticmethod
    def __compress_first_step(node: Node, parent: Node, next_hop: int):
        if node is None:
            # reached a leaf in the tree
            # store in the leaf a set of next-hop for this prefix
            # this accesses the private variable intentionally
            parent.next_hop = {next_hop}
        else:
            # if node has only one child: create the missing child
            if node.left and not node.right:
                # this node has only a left child: create the right child
                node.right = Node(next_hop)
            elif node.right and not node.left:
                # this node has only a right child: create the left child
                node.left = Node(next_hop)

            if node.next_hop:
                # store the current next-hop for nodes under this node
                next_hop = node.next_hop
                # unset this node next-hop
                node.clear_next_hop()

            # go to the left node
            BinaryTree.__compress_first_step(node.left, node, next_hop)
            # go to the right node
            BinaryTree.__compress_first_step(node.right, node, next_hop)

    @staticmethod
    def __operation(next_hops1, next_hops2):
        try:
            intersection = next_hops1.intersection(next_hops2)
        except AttributeError:
            # the first next hops is not a set but an int
            next_hops1 = {next_hops1}
            intersection = next_hops1.intersection(next_hops2)
        except TypeError:
            # the second next hops is not a set but an int
            next_hops2 = {next_hops2}
            intersection = next_hops1.intersection(next_hops2)

        if len(intersection) == 0:
            new_set = next_hops1.union(next_hops2)
        else:
            new_set = intersection
        return new_set

    @staticmethod
    def __operation_node(node):
        if node is None:
            return {}
        else:
            return BinaryTree.__operation(BinaryTree.__operation_node(node.left),
                                          BinaryTree.__operation_node(node.right))

    @staticmethod
    def __expand_node(node, next_hop):
        if node.left and not node.right:
            node.right = Node(next_hop)
            node.clear_next_hop()
        elif not node.left and node.right:
            node.left = Node(next_hop)
            node.clear_next_hop()

    @staticmethod
    def __get_next_hops(node: Node):
        """
        :rtype : set
        """

        if node.next_hop:
            # reached a leaf
            return node.next_hop
        else:
            # get the next-hops of the left node
            left_next_hops = BinaryTree.__get_next_hops(node.left)
            # get the next-hops of the right node
            right_next_hops = BinaryTree.__get_next_hops(node.right)

            # compute the current next-hop set
            node._next_hop = BinaryTree.__operation(left_next_hops, right_next_hops)
            # return the set of next-hops of this node
            return node.next_hop

    @staticmethod
    def __choose_next_hop(node: Node, parent: Node, next_hop, left: bool):

        if node:
            # check if the inherent next-hop is in the next-hop set of the node
            if next_hop in node.next_hop:
                # the node doesn't need it's own next-hop

                if len(node.next_hop) == 1:
                    # this node is not necessary anymore: remove the node
                    if left:
                        parent.clear_left()
                    else:
                        parent.clear_right()
                    node.clear_left()
                    node.clear_right()

                else:
                    # this node is necessary and is a blank node
                    node.clear_next_hop()
            else:
                # choose one of the possible next-hops of the node
                node.next_hop = node.next_hop.pop()
                next_hop = node.next_hop

            # move to the left node
            BinaryTree.__choose_next_hop(node.left, node, next_hop, True)
            # move to the right node
            BinaryTree.__choose_next_hop(node.right, node, next_hop, False)
