import Heap as hp
import graphTheory as gt
import Stack as st


def find_hamil_path(edge_list, start):
    edges = {(u, v): weight for u, v, weight in edge_list}
    path = [start]
    visited = {start}

    v_set = set(u for u, v, _ in edge_list).union(v for u, v, _ in edge_list)

    while len(path) < len(v_set):
        neighbors = [(weight, v if u == path[-1] else u)
                     for (u, v), weight in edges.items()
                     if u == path[-1] or v == path[-1]]

        hp.buildMinHeap(neighbors)

        while neighbors:
            weight, next_v = neighbors.pop(0)
            if next_v not in visited:
                visited.add(next_v)
                path.append(next_v)
                break
        else:
            return None  # If no unvisited neighbors exist, return None

    return path


def find_hamil_circuit(edge_list, start):
    path = find_hamil_path(edge_list, start)
    if path:
        edges = [(u, v) for u, v, _ in edge_list]
        if (path[-1], start) in edges or (start, path[-1]) in edges:
            path.append(start)  # Close the circuit
            return path
    return None


def mst_hamil_circuit(edge_list):
    kruskal = gt.Kruskal()
    for u, v, weight in edge_list:
        kruskal.kEdge(u, v, weight)

    mst, _ = kruskal.runKruskal()
    mst_edges = [(u, v) for u, v, _ in mst]

    visited = set()
    circuit = []
    stack = st.Stack()

    start_v = edge_list[0][0] if edge_list else None
    if start_v is None:
        print("No vertices in the graph.")
        return []
    stack.push(start_v)

    while not stack.isEmpty():
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            circuit.append(vertex)
            for u, v in mst_edges:
                next_v = None
                if u == vertex and v not in visited:
                    next_v = v
                elif v == vertex and u not in visited:
                    next_v = u

                if next_v is not None:
                    stack.push(next_v)

    if circuit:
        circuit.append(circuit[0])

    return circuit
