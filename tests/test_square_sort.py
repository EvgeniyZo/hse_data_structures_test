from main.square_sort import sort

def test_sort():
    arr = [5, 1, 7, 8, 5, 3, 4, 2]
    sort(arr)
    assert arr == [1, 2, 3, 4, 5, 5, 7, 8]
