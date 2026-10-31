graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


def dls(current, target, depth, route):

    if current == target:
        return "FOUND", route

    if depth == 0:
        if graph[current]:
            return "CUTOFF", None
        return "FAILURE", None

    cutoff_found = False

    for neighbor in graph[current]:

        if neighbor not in route:

            status, result = dls(
                neighbor, target, depth - 1, route + [neighbor]
            )

            if status == "FOUND":
                return status, result

            if status == "CUTOFF":
                cutoff_found = True

    if cutoff_found:
        return "CUTOFF", None

    return "FAILURE", None


def iddfs(source, target, maximum_depth):

    for depth_limit in range(maximum_depth + 1):

        status, result = dls(source, target, depth_limit, [source])

        print("Limit:", depth_limit, "Status:", status)

        if status == "FOUND":
            print("Path:", result)
            return result


iddfs("A", "G", 4)