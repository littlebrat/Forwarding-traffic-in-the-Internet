class Node():

    def __init__(self,hopValue = -1):
        self.nextHop = hopValue
        self.left = None
        self.right = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self,node):
        self.left = node

    def setRight(self,node):
        self.right = node

    def getHop(self):
        return self.nextHop


