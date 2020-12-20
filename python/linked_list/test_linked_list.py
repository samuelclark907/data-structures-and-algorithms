from linked_list.linked_list import LinkedList, Node
import pytest

a = Node(2)
def testone():
    assert (a.value ==2 and a.next is None)

b = LinkedList()
c = LinkedList(1)
def testtwo():
    assert c.head.value == 1

def testthree():
    assert c.head.next == None

def testfour():
    b.insert(5)
    assert b.head.value == 5