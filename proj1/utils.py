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

    def set_left(self,node):
        self._left = node

    def set_right(self,node):
        self._right = node

    def get_hop(self):
        return self._next_hop

    def set_next_hop(self, next_hop):
        self._next_hop = next_hop

    def __str__(self):
        return '(' + str(self.id) + ', ' + str(self._next_hop) + ')'

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def is_empty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0
