import pytest
from quick_sort import QuickSort, Partition

def test_quick_sort():
    lst = [6,5,4,3,2,1]
    n = len(lst)
    actual = QuickSort(lst, 0, n-1)
    expected = [1,2,3,4,5,6]
    assert actual == expected