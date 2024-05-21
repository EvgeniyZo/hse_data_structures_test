from collections import deque

class node:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

queue = deque()

def bfs(g, value):
    if (g.left is not None):
        queue.append(g.left)
    if (g.right is not None):
        queue.append(g.right)
    if (g.value == value):
        return True
    if (len(queue) == 0):
        return False
    next = queue.popleft()
    return bfs(next, value)

#preorder
def dfs_preorder(g, value):
    if (g is None):
        return False
    if (g.value == value):
        return True
    return dfs_preorder(g.left, value) or dfs_preorder(g.right, value)

#in order
def dfs_inorder(g, value):
    if (g is None):
        return False
    res = dfs_inorder(g.left, value)
    if (g.value == value):
        return True
    res |= dfs_inorder(g.right, value)
    return res

#postorder
def dfs_postorder(g, value):
    if (g is None):
        return False
    res = dfs_postorder(g.left, value)
    res |= dfs_postorder(g.right, value)
    if (g.value == value):
        return True
    return res