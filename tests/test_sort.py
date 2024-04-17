from main.sort import sort


def test_sort():
    arr = [5, 1, 7, 8, 3, 4, 2]
    print(sorted(arr))
    assert sort(arr) == [1, 2, 3, 4, 5, 7, 8]
