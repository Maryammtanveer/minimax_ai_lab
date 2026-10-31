import heapq

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}

heuristic = {
    "S": 5,
    "A": 4,
    "B": 4,
    "C": 2,
    "G": 0
}

def search(source, destination, h):

    queue = [(h[source], 0, source, [source])]
    distance = {source: 0}
    visited = []

    while queue:

        priority, cost, current, route = heapq.heappop(queue)

        if cost != distance[current]:
            continue

        visited.append(current)

        print("Processed:", current, "g:", cost, "h:", h[current], "f:", priority)

        if current == destination:
            return route, cost, visited

        for neighbor, edge_cost in graph[current]:

            total_cost = cost + edge_cost

            if total_cost < distance.get(neighbor, float("inf")):

                distance[neighbor] = total_cost

                new_priority = total_cost + h[neighbor]

                heapq.heappush(
                    queue,
                    (new_priority, total_cost, neighbor, route + [neighbor])
                )

    return None, float("inf"), visited


print("A* Search")

astar_route, astar_total, astar_visited = search("S", "G", heuristic)

print("A* Path:", astar_route)
print("A* Cost:", astar_total)
print("A* Processed:", astar_visited)


print("\nUCS Search")

zero_heuristic = {node: 0 for node in graph}

ucs_route, ucs_total, ucs_visited = search("S", "G", zero_heuristic)

print("UCS Path:", ucs_route)
print("UCS Cost:", ucs_total)
print("UCS Processed:", ucs_visited)
 