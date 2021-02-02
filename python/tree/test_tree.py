import pytest
from tree import BinarySearchTree, BinaryTree, Node

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

tree = BinaryTree()
a.left = b 
a.right = c
tree.root = a 
b.left = d
b.right = e 
c.left = f 


bitree = BinarySearchTree()
bitree.add(10)
bitree.add(20)
bitree.add(30)
bitree.add(9)
bitree.add(7)

tritree = BinarySearchTree()
tritree.add(2)

emptytree = BinarySearchTree()

def test_add():
    assert bitree.root.value == 10
    assert bitree.root.right.value == 20
    assert bitree.root.right.right.value == 30
    assert bitree.root.left.value == 9
    assert bitree.root.left.left.value == 7

def test_contains():
    expected = True
    actual = bitree.contains(10)
    assert expected == actual
    # assert bitree.contains(7)

def test_pre_order():
    actual = tree.pre_order()
    expected = ['A', 'B', 'D', 'E', 'C', 'F']
    assert actual == expected

def test_in_order():
    actual = tree.in_order()
    expected = ['D', 'B', 'E', 'A', 'F', 'C']
    assert actual == expected

def test_post_order():
    actual = tree.post_order()
    expected = ['D', 'E', 'B', 'F', 'C', 'A']
    assert actual == expected

def test_single_node():
    assert tritree.root.value == 2

def test_empty_tree():
    assert emptytree.root == None

def test_max_value():
    assert bitree.find_maximum_value() == 30
