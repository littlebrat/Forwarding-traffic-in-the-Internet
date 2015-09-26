from utils import Node, Queue


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
                    cur_node.setRight(Node(-1))
                # move the current node to the right node
                cur_node = cur_node.right()
            else:
                # move to the left
                if cur_node.left() is None:
                    # create node if necessary
                    cur_node.setLeft(Node(-1))
                # move the current node to the left node
                cur_node = cur_node.left()
        # set the next-hop of the final node
        cur_node.set_next_hop(next_hop)

    def lookup(self,prefix):
        # starting point for the search
        cur_node = self.root
        for bit in prefix:
            if bit is '1':
                # move to the right
                if cur_node.right() is None:
                    # if there is not any node right, longest prefix has been found
                    return cur_node.getHop()
                    # return the nextHop for this ip
                # move right
                cur_node = cur_node.right()
            else:
                # move to the left
                if cur_node.left() is None:
                    # if there is not any node left, longest prefix has been found
                    return cur_node.getHop()
                    # return the nextHop for this ip
                # move left
                cur_node = cur_node.left()


    def __str__(self):
        cur_node = self.root


