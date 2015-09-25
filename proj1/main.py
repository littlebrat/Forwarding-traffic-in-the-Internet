from binarytree import BinaryTree

test = BinaryTree(1)

test.insert('00',2)
test.insert('10',2)
test.insert('11',3)
test.insert('010',3)
test.insert('110',4)

print(test.root.right().right().left())

