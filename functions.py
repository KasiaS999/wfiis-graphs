import networkx as nx
import matplotlib.pyplot as plt


def check_graphic_sequence(seq):
    seq = list(seq)
    seq.sort(reverse=True)
    while True:
        if all(number == 0 for number in seq):
            return True
        if any(number < 0 for number in seq) or seq[0] >= len(seq):
            return False
        for i in range(1, seq[0]+1):
            seq[i] -= 1
        seq[0] = 0
        seq.sort(reverse=True)


def generate_path(prev, index):
    path = [index]
    prev_index = prev[index]
    while prev_index is not None:
        path.append(prev_index)
        index = prev_index
        prev_index = prev[index]

    return path


def print_S(S, d, p):
    print(f'START: s = {S[0]}')
    for i in S:
        path = generate_path(p, i)
        print(f'd({i}) = {d[i]} ==> [', end='')
        for node in reversed(path):
            if node == path[0]:
                print(f' {node} ]')
            else:
                print(f' {node} -', end='')


def find_node_with_smallest_d(S, d):
    # not accepted node with smallest distance
    node = 0
    smallest_distance = float('inf')
    for i, distance in enumerate(d):
        if i not in S:
            if smallest_distance > distance:
                node = i
                smallest_distance = distance
    return node


def generate_and_draw_graph_with_weight(graph, l1, l2):
    graph.generate_random_coherent_graph(l1, l2)
    graph.add_random_weight()
    graph.draw_nx_graph_with_weight()


def print_matrix(matrix):
    for source in matrix:
        print(f'\033[1m{source}\033[0m', end=' ')
        for node in matrix[source]:
            print('{0: >4}'.format(node), end='')
        print()


##### ex 4 #####

def center_of_graph(matrix):
    center = -1
    min_sum = float('inf')
    for source in matrix:
        new_sum = sum(matrix[source])
        if min_sum > new_sum:
            min_sum = new_sum
            center = source
    print(f'Centrum: {center} (suma odległości: {min_sum})')


def minimax(matrix):
    minmax_source = -1
    min_max = float('inf')
    for source in matrix:
        max_value = max(matrix[source])
        if max_value < min_max:
            min_max = max_value
            minmax_source = source
    print(f'Centrum minimax = {minmax_source} ( odleglosc od najdalszego :'
          f' {min_max})')


def check_node_prim(start, end, selected, W_numbers):
    if start == selected:
        if end in W_numbers:
            return True
    if end == selected:
        if start in W_numbers:
            return True
    return False


def draw_minimum_spanning_tree(graph):
    G = nx.Graph()
    for node in graph.nodes:
        G.add_node(node.number)
    for edge, weight in zip(graph.edges, graph.weight):
        G.add_edge(edge.start, edge.end, weight=weight)
    T = nx.minimum_spanning_tree(G)
    pos = nx.spring_layout(T)
    plt.figure()
    nx.draw_networkx(T, pos=pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(T, 'weight')
    nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
    plt.show()


