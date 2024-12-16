# Robert Plastina
# Translates networkX to normal python lists.
# networkX is for display only, not solving the graphs.

import networkx as nx

def nx_to_adjlist(graph):
    adj_list = {node: list(neighbors) for node, neighbors in graph.adj.items()}
    return adj_list


def nx_to_edgelist(graph):
    edge_list = []
    for u, v, data in graph.edges(data=True):
        weight = data.get('weight', 1)  # Default weight = 1 if not specified
        edge_list.append((u, v, weight))
    return edge_list


def adjlist_to_nx(adj_list):
    graph = nx.Graph()
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            graph.add_edge(node, neighbor)
    return graph

def m_adjlist_to_nx(adj_list):
    m_graph = nx.MultiGraph()
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            m_graph.add_edge(node, neighbor)
    return m_graph


def edgelist_to_nx(edge_list):
    graph = nx.Graph()
    for src, dest, weight in edge_list:
        graph.add_edge(src, dest, weight=weight)
    return graph