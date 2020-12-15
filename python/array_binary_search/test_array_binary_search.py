

from array_binary_search.array_binary_search import binary_search

arr = [1,2,3,4,6,9]

def test_one():
    actual = binary_search(arr, 3)
    expected = 2
    assert actual == expected


def test_two():
    actual = binary_search(arr, 9)
    expected = 5
    assert actual == expected


def test_three():
    actual = binary_search(arr, 19)
    expected = -1
    assert actual == expected