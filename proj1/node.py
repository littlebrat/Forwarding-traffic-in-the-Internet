class Node:
    id_count = 0

    def __init__(self, next_hop=-1, left=None, right=None):
        self._next_hop = next_hop
        self._left = left
        self._right = right
        self.id = Node.id_count
        Node.id_count += 1

    def next_hop(self):
        return self._next_hop

    def set_next_hop(self, next_hop):
        self._next_hop = next_hop

    def left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    def right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    def __str__(self):
        return '(' + str(self.id) + ', ' + str(self._next_hop) + ')'

    def __eq__(self, other):
        return self.id == other.id
