def dijkstra(graph: dict, start: str, end: str):
    processed_nodes = []

    distance_from_start: dict[str, int | float] = {
        k: (graph[start][k] if k in graph[start] else float("inf"))
        for k, v in graph.items()
    }

    parents: dict = {end: None}

    for node in graph[start]:
        parents[node] = start

    node = find_shortest_path(distance_from_start, processed_nodes)

    while node is not None:
        distance: int | float = distance_from_start[node]
        neighbors = graph[node]
        for n in neighbors:
            new_distance = distance + neighbors[n]
            if distance_from_start[n] > new_distance:
                distance_from_start[n] = new_distance
                parents[n] = node
        processed_nodes.append(node)
        node = find_shortest_path(distance_from_start, processed_nodes)

    return distance_from_start[end]


def find_shortest_path(distance_from_start: dict, processed_nodes: list):
    lowest_distance = float("inf")
    lowest_distance_node = None

    for node in distance_from_start:
        distance = distance_from_start[node]

        if distance < lowest_distance and node not in processed_nodes:
            lowest_distance = distance
            lowest_distance_node = node
    return lowest_distance_node


if __name__ == "__main__":
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 10, "D": 1},
        "C": {"D": 5},
        "D": {"E": 3, "F": 8},
        "E": {"F": 1},
        "F": {},
    }

    dijkstra(graph, "A", "F")
