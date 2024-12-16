import networkx as nx
import matplotlib.pyplot as plt
import nxcom as xc
import Hamilton as ha


def p15(in_nx):

    edge_list = xc.nx_to_edgelist(in_nx)
    circuit = ha.find_hamil_circuit(edge_list, start=0)
    if circuit:
        print("Hamilton Circuit:", circuit)
        pos = nx.spring_layout(in_nx)
        nx.draw(in_nx, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
        edge_path = [(circuit[i], circuit[i + 1]) for i in range(len(circuit) - 1)]
        nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='blue', width=2)
        plt.title("Hamilton Circuit")
        plt.show()
    else:
        print("No Hamilton Circuit Found.")

def p16(in_nx):

    edge_list = xc.nx_to_edgelist(in_nx)
    path = ha.find_hamil_path(edge_list, start=0)
    if path:
        print("Hamilton Path:", path)
        pos = nx.spring_layout(in_nx)
        nx.draw(in_nx, pos, with_labels=True, node_color='lightgreen', edge_color='gray')
        edge_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(in_nx, pos, edgelist=edge_path, edge_color='blue', width=2)
        plt.title("Hamilton Path")
        plt.show()
    else:
        print("No Hamilton Path Found.")

def main():

    in_list1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3), (2, 4)]
    in_list2 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 2), (3, 5)]

    G1 = nx.Graph()
    G1.add_edges_from(in_list1)
    p15(G1)

    G2 = nx.Graph()
    G2.add_edges_from(in_list2)
    p15(G2)


main()

