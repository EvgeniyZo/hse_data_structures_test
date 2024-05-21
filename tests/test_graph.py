import pytest
from main.graph import node, bfs, dfs_inorder, dfs_postorder, dfs_preorder

# *
# |\
# * *
# |\ \ 
# * * \
# |    \
# *     *
#       |\
#       * *
#         |
#         *



@pytest.mark.parametrize("x, expected", [
    (5, True),
    (11, False),
    (-1, False),
    (7, True),
    (1, True),
])
def test_bfs(x, expected):
    g = node(node(node(node(None, None, 1), None, 2), node(None, None, 4), 3), node(None, node(node(None, None, 7), node(None, node(None, None, 10), 9), 8), 6), 5)
    assert bfs(g, x) == expected

@pytest.mark.parametrize("x, expected", [
    (5, True),
    (11, False),
    (-1, False),
    (7, True),
    (1, True),
])
def test_dfs_preorder(x, expected):
    g = node(node(node(node(None, None, 1), None, 2), node(None, None, 4), 3), node(None, node(node(None, None, 7), node(None, node(None, None, 10), 9), 8), 6), 5)
    assert dfs_preorder(g, x) == expected

@pytest.mark.parametrize("x, expected", [
    (5, True),
    (11, False),
    (-1, False),
    (7, True),
    (1, True),
])  
def test_dfs_inorder(x, expected):
    g = node(node(node(node(None, None, 1), None, 2), node(None, None, 4), 3), node(None, node(node(None, None, 7), node(None, node(None, None, 10), 9), 8), 6), 5)
    assert dfs_inorder(g, x) == expected

@pytest.mark.parametrize("x, expected", [
    (5, True),
    (11, False),
    (-1, False),
    (7, True),
    (1, True),
])
def test_dfs_postorder(x, expected):
    g = node(node(node(node(None, None, 1), None, 2), node(None, None, 4), 3), node(None, node(node(None, None, 7), node(None, node(None, None, 10), 9), 8), 6), 5)
    assert dfs_postorder(g, x) == expected
