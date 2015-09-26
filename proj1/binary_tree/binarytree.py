from proj1.node import Node


class BinaryTree:

    def __init__(self, default_next_hop):
        # start with only one node with the default next-hop
        self.root = Node(default_next_hop)

    def insert(self, prefix, next_hop):
        cur_node = self.root
        for bit in prefix:
            if bit is '1':
                # move to the right
                if cur_node.right() is None:
                    # create node if necessary
                    cur_node.set_right(Node(-1))
                # move the current node to the right node
                cur_node = cur_node.right()
            else:
                # move to the left
                if cur_node.left() is None:
                    # create node if necessary
                    cur_node.set_left(Node(-1))
                # move the current node to the left node
                cur_node = cur_node.left()
        # set the next-hop of the final node
        cur_node.set_next_hop(next_hop)

    def lookup(self, ip):
        # starting point for the search
        cur_node = self.root
        hop = cur_node.next_hop()
        for bit in ip:
            if bit is '1':
                # memorize the hop if it is valid
                if cur_node.next_hop() != -1:
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
                if cur_node.next_hop() != -1:
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
            if bit is '1':
                # find if the current node has 2 children
                if cur_node.right() is not None and cur_node.left() is not None:
                    parent, side = cur_node, '1'
                # move to the right
                cur_node = cur_node.right()
            else:
                # find if the current node has 2 children
                if cur_node.right() is not None and cur_node.left() is not None:
                    parent, side = cur_node, '0'
                # move to the left
                cur_node = cur_node.left()
        if cur_node.right() is not None or cur_node.left() is not None:
            cur_node.set_next_hop(-1)
        else:
            if side is '1':
                # delete the right child of the tree
                parent.set_right(None)
            elif side is '0':
                # delete the left child of the tree
                parent.set_left(None)

    def __str__(self):
        cur_node = self.root
