class Node():
    id_count = 0

    def __init__(self,hopValue = -1, left=None, right=None):
        self._next_hop = hopValue
        self._left = left
        self._right = right
        self.id = Node.id_count
        Node.id_count += 1

    def left(self):
        return self._left

    def right(self):
        return self._right

    def setLeft(self,node):
        self._left = node

    def setRight(self,node):
        self._right = node

    def getHop(self):
        return self._next_hop

    def set_next_hop(self, next_hop):
        self._next_hop = next_hop

    def __str__(self):
        return '(' + str(self.id) + ', ' + str(self._next_hop) + ')'


