import pytest
from main.fib import fib

@pytest.mark.parametrize("x, expected", [
    (0, None),
    (1, 0),
    (2, 1),
    (3, 2),
    (4, 4),
    (10, 34),
    (24, 28657),
    (200, 173402521172797813159685037284371942044301),
    (-5, None),
    (float("inf"), None),
    (float("-inf"), None),
    ("abc", None),
    (None, None)
])
def test_fib(x, expected):
    assert fib(x) == expected
