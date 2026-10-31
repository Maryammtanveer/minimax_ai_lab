from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

def bfs(source, target):

    waiting_list = deque([(source, [source])])
    visited = {source}
    visit_order = []

    while waiting_list:

        current, route = waiting_list.popleft()
        visit_order.append(current)

        if current == target:
            return route, visit_order

        for neighbor in graph[current]:

            if neighbor not in visited:
                visited.add(neighbor)
                waiting_list.append((neighbor, route + [neighbor]))

    return None, visit_order


def dfs(source, target):

    stack = [(source, [source])]
    visited = set()
    visit_order = []

    while stack:

        current, route = stack.pop()

        if current in visited:
            continue

        visited.add(current)
        visit_order.append(current)

        if current == target:
            return route, visit_order

        for neighbor in reversed(graph[current]):
            stack.append((neighbor, route + [neighbor]))

    return None, visit_order


bfs_route, bfs_visited = bfs("A", "G")
dfs_route, dfs_visited = dfs("A", "G")

print("BFS Visit Order:", bfs_visited)
print("BFS Path:", bfs_route)

print("\nDFS Visit Order:", dfs_visited)
print("DFS Path:", dfs_route)
 
