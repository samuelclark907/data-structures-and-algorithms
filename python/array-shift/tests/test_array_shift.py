from array_shift import __version__

from array_shift.array_shift import insertShiftArray


def test_version():
    assert __version__ == '0.1.0'


arr = [1,2,3,4]
bar = [1,2,3,4,5,6,7,8]


def testone():
    actual = insertShiftArray(arr,9)
    expected = [1,2,9,3,4]
    assert actual == expected


def testtwo():
    actual = insertShiftArray(bar,9)
    expected = [1,2,3,4,9,5,6,7,8]
    assert actual == expected