import sys
import csv
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from netgraph import Graph # pip install netgraph


def main():
    if len(sys.argv) == 1:
        print("Doğru komutu giriniz -> python graph_visualizer.py <filename>")
        return

    filename = sys.argv[1]
    adjacency_matrix, weights = get_adjacency_matrix(filename)
    graph = set_graph(adjacency_matrix)
    draw_graph(graph, weights)
    # print(adjacency_matrix)


def get_adjacency_matrix(filename):
    adjacency_matrix = []
    weights = {}
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                # print("i = ", i)
                # print("row = ", row)
                row = row[1:]  
                row_values = []
                for j, value in enumerate(row):
                    # print(list(enumerate(row)))
                    # print("j = ", j)
                    # print("value = ", value)
                    weight = int(value)
                    row_values.append(weight)
                    if weight != 0:
                        weights[(i + 1, j + 1)] = weight
                adjacency_matrix.append(row_values)
    except IOError as e:
        print("Dosya Okunamadı:", str(e))
    # print(weights)
    return adjacency_matrix, weights


def set_graph(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    graph = nx.DiGraph()  #nx.Graph() undirected
    graph.add_nodes_from(range(1, num_nodes + 1))
    for i in range(num_nodes):
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                graph.add_edge(i + 1, j + 1)
    return graph


def draw_graph(graph, weights):
    if (3 >= graph.number_of_nodes() >= 1000):
        print("Graph en az 3 en fazla 1000 node içermeli")
        return
    pos = nx.spring_layout(graph)  #diğer layoutlar mevcut: spring_layout, random_layout, shell_layout, circular_layout
    nx.draw_networkx(   #nx.draw() undirected
        graph,
        pos,
        with_labels=True,
        node_size=1000,
        node_color="skyblue",
        font_size=10,
        edge_color="gray",
    )
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights, label_pos=0.3, font_size=7)
    plt.title("Our Graph")
    plt.show()


if __name__ == "__main__":
    main()

    

    # nx.draw_spring(nx.Graph(), with_labels=True)
    # plt.show()