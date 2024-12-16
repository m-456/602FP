# Robert Plastina
# Answers 13. Shows both either a Circuit, Path, or Neither, and creates

import networkx as nx
import matplotlib.pyplot as plt
import nxcom as xc
import Euler as eu


def p13(in_nx):

    adj_list = xc.nx_to_adjlist(in_nx)

    if eu.has_euler_circuit(adj_list):
        circuit = eu.construct_euler_circuit(adj_list)
        print("Euler Circuit:", circuit)

        pos = nx.spring_layout(in_nx)
        nx.draw(in_nx, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        edge_path = [(circuit[i], circuit[i+1]) for i in range(len(circuit)-1)]
        nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='red', width=2)
        plt.title("Euler Circuit")
        plt.show()

    elif eu.has_euler_path(adj_list):
        print("No Euler Circuit.")
        path = eu.construct_euler_path(adj_list)
        print("Euler Path:", path)

        pos = nx.spring_layout(in_nx)
        nx.draw(in_nx, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        edge_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='red', width=2)
        plt.title("Euler Path")
        plt.show()
    else:
        print("No Euler Path or Circuit.")

def main():

    in_list = [(0, 1), (1, 2), (2, 3), (3, 1), (1, 4)]
    mvG = nx.MultiGraph()
    mvG.add_edges_from(in_list)
    # Modify this list
    p13(mvG)

main()