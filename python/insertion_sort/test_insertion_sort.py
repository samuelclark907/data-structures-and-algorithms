from .insertion_sort import insertion_sort
input = [8,4,23,42,16,15]

def test_insertion_sort():
    actual = insertion_sort(input)
    expected = [4,8,15,16,23,42]
    assert actual == expected