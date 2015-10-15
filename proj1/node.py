class Node:
    _id_count = 0

    def __init__(self, next_hop=None, left=None, right=None):
        self._next_hop = next_hop
        self._left = left
        self._right = right
        self._id = Node._id_count
        Node._id_count += 1

    @property
    def next_hop(self):
        return self._next_hop

    @next_hop.setter
    def next_hop(self, value):
        self._next_hop = value

    def clear_next_hop(self):
        self.next_hop = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    def clear_left(self):
        self.left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    def clear_right(self):
        self.right = None

    def clear_children(self):
        self.left = None
        self.right = None

    def copy(self, dest_node=None):
        """
         Copies the self node information (including the id) into the dest_node node.
         If a destination node is not provided a new one is created and returned.
         It doesn't copy the references to the child nodes, those are kept undefined.
        :type dest_node: Node
        :rtype : Node
        """

        if dest_node is None:
            node = Node(self.next_hop)
        else:
            dest_node.next_hop = self.next_hop
            # return the destination node
            node = dest_node

        Node._id_count -= 1
        node._id = self._id
            
        return node

    def __str__(self):
        return '(' + str(self._id) + ', ' + str(self.next_hop if self.next_hop else '') + ')'

    def __eq__(self, other):
        """
        :type other: Node
        """
        return self._id == other._id
