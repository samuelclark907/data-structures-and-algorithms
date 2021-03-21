from tree_intersection import tree_intersection, BinaryTree, Node

a = Node("1")
b = Node("2")
c = Node("3")
d = Node("4")
e = Node("5")
f = Node("6")

g = Node("1")
h = Node("6")
i = Node("1")
j = Node("10")
k = Node("11")
l = Node("12")

tree1 = BinaryTree()
a.left = b 
a.right = c
tree1.root = a 
b.left = d
b.right = e 
c.left = f

tree2 = BinaryTree()
g.left = h 
g.right = i
tree2.root = g 
h.left = j
h.right = k 
i.left = l

def test_tree_intersection():
    assert tree_intersection(tree1,tree2) == ["1","6"]