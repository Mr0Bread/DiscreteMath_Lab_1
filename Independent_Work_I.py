import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

first_graph = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0],  # 1
    [0, 0, 0, 1, 0, 1, 0, 0],  # 2
    [0, 0, 0, 0, 1, 1, 0, 0],  # 3
    [0, 0, 0, 0, 0, 1, 0, 0],  # 4
    [0, 0, 0, 0, 0, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0]  # 7
])

second_graph = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],  # 1
    [0, 0, 0, 0, 0, 0, 0, 0],  # 2
    [0, 0, 1, 0, 0, 0, 0, 0],  # 3
    [0, 0, 0, 0, 0, 1, 0, 0],  # 4
    [0, 1, 0, 1, 1, 0, 0, 0],  # 5
    [0, 0, 0, 0, 0, 0, 0, 0],  # 6
    [0, 0, 0, 0, 0, 0, 0, 0]  # 7
])

simple_G = nx.from_numpy_matrix(first_graph)
directed_G = nx.from_numpy_matrix(second_graph, create_using=nx.DiGraph)

simple_G.remove_node(0)
directed_G.remove_node(0)


def compute_and_display_neighbors(graph):
    for x in range(1, len(graph) + 1):
        for i in graph.neighbors(x):
            print("Node: ", x, "Neighbor: ", i)


def compute_and_display_degrees(simple_graph):
    for x in range(1, len(simple_graph) + 1):
        print("Node: ", x, "Number of degrees: ", simple_graph.degree[x])


def print_sum_of_degrees(simple_graph):
    result = 0

    for x in range(1, len(simple_graph) + 1):
        result += simple_graph.degree[x]
    else:
        print('Result of degrees:', result)


def print_indegrees_and_out_degrees(directed_graph):
    for x in range(1, len(directed_graph) + 1):
        print("Node: ", x, "Indegrees: ", directed_graph.in_degree(x), "Outdegrees: ", directed_graph.out_degree(x))


def print_edge_list(graph):
    print(graph.edges)


def print_list_of_vertices(list_of_edges):
    print(nx.Graph(list_of_edges).nodes)


def show_graph(graph):
    nx.draw_circular(graph, with_labels=True)
    plt.show()

