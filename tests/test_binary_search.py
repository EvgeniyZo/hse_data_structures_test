from main.binary_search import binary_search


def test_binary_search():
    arr = [3, 12, 13, 49, 67, 321]

    assert binary_search(arr, 67) == 4
    assert binary_search(arr, 999) is None
