from main.binsearch import binsearchl, binsearchr

def test_binsearchl():
    num = 9
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    assert binsearchl(arr, num) == 6

def test_binsearchr():
    num = 9
    arr = [1, 2, 3, 3, 7, 8, 9, 9, 9, 11]
    assert binsearchr(arr, num) == 8
