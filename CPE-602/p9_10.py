# Robert Plastina
# Combines P9 and P10

import networkx as nx
import matplotlib.pyplot as plt
import nxcom as xc
import Euler as eu
import Hamilton as ha
import random


def random_graph(vertices=10, edge_prob=0.5):
    return nx.erdos_renyi_graph(vertices, edge_prob)

def p9():
    while True:
        in_nx = nx.Graph()
        in_nx.add_nodes_from(range(10))  # Add 10 vertices
        for _ in range(20):  # Randomly add edges
            u, v = random.sample(range(10), 2)
            in_nx.add_edge(u, v)
        adj_list = xc.nx_to_adjlist(in_nx)
        if eu.has_euler_circuit(adj_list):
            print("Found an Euler Circuit.")
            circuit = eu.construct_euler_circuit(adj_list)

            # Display the Euler Circuit using NetworkX
            pos = nx.spring_layout(in_nx)
            nx.draw(in_nx, pos, with_labels=True, node_color='lightblue', edge_color='gray')
            edge_path = [(circuit[i], circuit[i + 1]) for i in range(len(circuit) - 1)]
            nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='red', width=2)
            plt.title("Euler Circuit")
            plt.show()
            break

def p10():
    while True:
        in_nx = nx.Graph()
        in_nx.add_nodes_from(range(10))  # Add 10 vertices
        for _ in range(20):  # Randomly add edges
            u, v = random.sample(range(10), 2)
            in_nx.add_edge(u, v)

        edge_list = xc.nx_to_edgelist(in_nx)
        circuit = ha.find_hamil_circuit(edge_list, start=0)
        if circuit:
            print("Found a Hamiltonian Circuit.")
            pos = nx.spring_layout(in_nx)
            nx.draw(in_nx, pos, with_labels=True, node_color='lightblue', edge_color='gray')
            edge_path = [(circuit[i], circuit[i + 1]) for i in range(len(circuit) - 1)]
            nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='red', width=2)
            plt.title("Hamilton Circuit")
            plt.show()
            break

def main():
    p9()
    p10()

main()






