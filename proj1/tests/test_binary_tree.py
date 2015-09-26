from proj1.routing_binary_tree import RoutingBinaryTree
from proj1.prefix import Prefix


def print_tree(tree):
    node = tree.root
    nodes = []
    while node:
        nodes.insert(0, node.left())
        nodes.insert(0, node.right())

        print("node: ", node)
        print("left: ", node.left())
        print("right: ", node.right())
        print()

        node = nodes.pop(len(nodes) - 1)

tree = RoutingBinaryTree(1)
print("initial")
print_tree(tree)

tree.insert(Prefix("00"), 2)
print("00->2")
print_tree(tree)

tree.insert(Prefix("10"), 2)
print("10->2")
print_tree(tree)

print(tree.lookup("255.1.1.1"), 1)
print(tree.lookup("0.1.1.1"), 2)
print(tree.lookup("127.1.1.1"), 1)
print(tree.lookup("64.1.1.1"), 1)
print(tree.lookup("128.1.1.1"), 2)
print(tree.lookup("160.1.1.1"), 2)