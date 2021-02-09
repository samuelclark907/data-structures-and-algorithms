from fizz_buzz_tree import fizz_buzz, fizz_buzz_tree, Tree, K_node

tree = Tree()
tree.root = K_node(1)
tree.root.child.append(K_node(2))
tree.root.child.append(K_node(3))
tree.root.child.append(K_node(4))
tree.root.child[0].child.append(K_node(5)) 
tree.root.child[0].child[0].child.append(K_node(10)) 
tree.root.child[0].child.append(K_node(6)) 
tree.root.child[0].child[1].child.append(K_node(11))
tree.root.child[0].child[1].child.append(K_node(12))
tree.root.child[0].child[1].child.append(K_node(15)) 
tree.root.child[2].child.append(K_node(7))
tree.root.child[2].child.append(K_node(8))
tree.root.child[2].child.append(K_node(9))


def test_fizz():
    thistree = fizz_buzz_tree(tree)
    actual = thistree.root.child[0].child[0]
    expected = "Buzz"
    assert actual == expected

def test_buzz():
    pass

def test_fizz_buzz():
    pass