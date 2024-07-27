my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

my_complex_graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2), ('E', 5)],
    'C': [('A', 1), ('F', 8), ('G', 7)],
    'D': [('B', 2), ('H', 6)],
    'E': [('B', 5), ('I', 3)],
    'F': [('C', 8), ('J', 3)],
    'G': [('C', 7), ('J', 6)],
    'H': [('D', 6), ('I', 1), ('J', 5)],
    'I': [('E', 3), ('H', 1)],
    'J': [('F', 3), ('G', 6), ('H', 5)]
}


def shortest_path(graph, start, target=''):
    # Initialize a list of unvisited nodes and a dictionary for distances and paths
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # Initialize the path for each node with the start node
    paths = {node: [] for node in graph}  # Create a list have key: value with value is empty list
    paths[start].append(start)

    # Loop until all nodes are visited
    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=distances.get)
        # Distances.get is passed as the key function to min().
        # This means for each node in unvisited, min() calls distances.get(node),
        # which returns the distance of that node from the start node.

        # Update the distance and path for each neighbor of the current node
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                    # The [:] syntax in Python is used for creating a shallow copy of a list. When used in the
                    # context paths[node] = paths[current][:], it means that the list referenced by paths[current] is
                    # copied element by element into a new list, and this new list is then assigned to paths[node].
                    # This ensures that paths[node] gets a separate list object, preventing unintended modifications
                    # to the list referenced by paths[current] when the list for paths[node] is modified.
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        # Mark the current node as visited
        unvisited.remove(current)

    # Print or return the distance and path to the target node or all nodes
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths


if __name__ == '__main__':
    shortest_path(my_graph, 'A', 'F')
    shortest_path(my_complex_graph, 'A')
