import graphTheory as gt
import Stack as st


def connected(adj_list):
    search = gt.GraphDFS()

    for src, neighbors in adj_list.items():
        for dest in neighbors:
            search.addEdge(src, dest)

        # Find the first vertex with edges
    start_v = next((v for v, neighbors in adj_list.items() if neighbors), None)
    if start_v is None:
        return True  # No edges, trivially connected

    discovery_time, _, _ = search.runDFS(start_v)
    visited_v = set(discovery_time.keys())
    return all(v in visited_v or not neighbors for v, neighbors in adj_list.items())


def has_euler_circuit(adj_list):
    if not connected(adj_list):
        return False  # Graph is not connected
    return all(len(neighbors) % 2 == 0 for neighbors in adj_list.values())


def has_euler_path(adj_list):
    if not connected(adj_list):
        return False  # Graph is not connected
    odd_degree = sum(1 for neighbors in adj_list.values() if len(neighbors) % 2 != 0)
    return odd_degree in [0, 2]


def construct_euler_circuit(adj_list):

    if not has_euler_circuit(adj_list):
        return []

    # Create a deep copy of the graph
    graph = {v: neighbors[:] for v, neighbors in adj_list.items()}
    traversal = st.Stack()
    circuit = []
    current_v = next((v for v, neighbors in graph.items() if neighbors), None)
    if current_v is None:
        return []

    traversal.push(current_v)

    while not traversal.isEmpty():
        current_v = traversal.peek()
        if graph[current_v]:  # If the current vertex has neighbors
            next_v = graph[current_v].pop()
            graph[next_v].remove(current_v)  # Remove the edge from both ends
            traversal.push(next_v)
        else:
            circuit.append(traversal.pop())

    return circuit[::-1]


def construct_euler_path(adj_list):

    if not has_euler_path(adj_list):
        return []  # No Euler path possible

    start_v = None
    for vertex, neighbors in adj_list.items():
        if len(neighbors) % 2 != 0:
            start_v = vertex
            break

    if start_v is None:
        start_v = next((v for v, neighbors in adj_list.items() if neighbors), None)

    if start_v is None:
        return []

    graph = {v: neighbors[:] for v, neighbors in adj_list.items()}
    stack = [start_v]
    path = []

    while stack:
        current_v = stack[-1]
        if graph[current_v]:
            next_v = graph[current_v].pop()
            graph[next_v].remove(current_v)
            stack.append(next_v)
        else:
            path.append(stack.pop())

    return path[::-1]
