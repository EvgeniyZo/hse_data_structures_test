# поиск в глубину
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited


# поиск в ширину
def bfs(graph, start):
    visited = set()
    visited.add(start)

    for neighbor in graph:
        neighbor_one = graph[neighbor]
        for i in neighbor_one:
            if i not in visited:
                visited.add(i)
    return visited


# Пример графа в виде словаря списков смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C'],
    'F': ['D'],
    'G': []
}
# Вывод в глубину
print(dfs(graph, 'A'))

# Вывод в ширину
print(bfs(graph, 'A'))
