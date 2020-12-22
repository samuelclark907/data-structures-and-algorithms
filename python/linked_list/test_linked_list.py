from linked_list.linked_list import LinkedList, Node
import pytest



a = Node(2)
b = LinkedList()
c = LinkedList(1)


def testone():
    assert (a.value ==2 and a.next is None)


def testtwo():
    assert c.head == 1


def testthree():
    c.insert(3)
    assert c.head.value == 3


def testfour():
    c.insert(5)
    assert c.head.value == 5


def testfive():
    assert c.includes(5) == True



