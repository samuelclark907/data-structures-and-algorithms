from linked_list.linked_list import LinkedList
from ll_zip import zipLists

def test_import():
    assert LinkedList


def test_same_length():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual = str(zipLists(ll1,ll2))
    expected = "{1}->{2}->{3}->{4}->{5}->{6}->None"
    assert actual == expected  


def test_diff_length():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    actual = str(zipLists(ll1,ll2))
    expected = "{1}->{2}->{3}->{4}->{5}->None"
    assert actual == expected  