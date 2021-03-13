import pytest
from merge_sort import merge, mergesort

def test_merge_sort():
    merge_list = [3,7,4,9,14,18,11]
    actual = mergesort(merge_list)
    expected = [3,4,7,9,11,14,18]
    assert actual == expected
    