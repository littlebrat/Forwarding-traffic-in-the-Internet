class Node:
    _id_count = 0

    def __init__(self, next_hop=None, left=None, right=None):
        self._next_hop = next_hop
        self._left = left
        self._right = right
        self._id = Node._id_count
        Node._id_count += 1

    def next_hop(self):
        return self._next_hop

    def set_next_hop(self, next_hop):
        self._next_hop = next_hop

    def unset_next_hop(self):
        self._next_hop = None

    def left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    def right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    def copy(self, dest_node=None):
        """
         Copies the self node information (including the id) into the dest_node node.
         If a destination node is not provided a new one is created and returned.
         It doesn't copy the references to the child nodes, those are kept undefined.
        :type dest_node: Node
        :rtype : Node
        """

        if dest_node is None:
            node = Node(self.next_hop())
        else:
            dest_node.set_next_hop(self.next_hop())
            # return the destination node
            node = dest_node

        node._id = self._id
            
        return node

    def __str__(self):
        return '(' + str(self._id) + ', ' + str(self._next_hop) + ')'

    def __eq__(self, other):
        """
        :type other: Node
        """
        return self._id == other._id
