from main.sort import sort


def test_sort():
    arr = [5, 1, 7, 8, 5, 3, 4, 2]
    print(sorted(arr))
    assert sort(arr) == sorted(arr)
