from main.dijkstra import dijkstra


def test_shortest_path():
    graph = {
        "A": {"B": 4, "C": 2},
        "B": {"C": 10, "D": 1},
        "C": {"D": 5},
        "D": {"E": 3, "F": 8},
        "E": {"F": 1},
        "F": {},
    }

    shortest_distance = dijkstra(graph, "A", "F")

    assert shortest_distance == 9
