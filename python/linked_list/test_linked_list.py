from linked_list.linked_list import LinkedList, Node
import pytest


# Code Challenge 05 tests

a = Node(2)
b = LinkedList()
c = LinkedList(1)


def testone():
    assert (a.value ==2 and a.next is None)


def testtwo():
    assert c.head == 1


def test_insert1():
    c.insert(3)
    assert c.head.value == 3


def test_insert2():
    c.insert(5)
    assert c.head.value == 5


def test_includes():
    assert c.includes(5) == True

# Code Challenge 06 tests


def test_append():
    newone_linked = LinkedList(Node(1))

    newone_linked.append(7)
    assert newone_linked.includes(7)


def test_insertBefore():
    newone_linked = LinkedList(Node(1))

    newone_linked.insertBefore(1,2)
    assert newone_linked.head.value == 2
    assert newone_linked.head.next.value == 1


def test_insertAfter():
    newone_linked = LinkedList(Node(1))
    newone_linked.insertAfter(1,3)
    assert newone_linked.head.value == 1
    assert newone_linked.head.next.value == 3
    
    

    

