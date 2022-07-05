"""
Approximating TSP using fast MST-Algorithms

Copyright 2020, University of Freiburg

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import heapq
import math
from AdjacencyMatrix import AdjacencyMatrix


def compute_tour(am):
    '''
        computes a tour which as an array tour[0],...,tour[n-1]
        containing the nodes {0,...,n-1}) of a graph given as
        Adjacency matrix that has a small sum of edge weights of
        a roundtrip defined as:
        w(tour[0],tour[1]) + ...
                           + w(tour[n-2],tour[n-1])
                           + w(tour[n-1],tour[0])
        the guarantee is that the weight of the computed tour
        is at most twice that of the best possible tour.

        Parameter:
            am - Instance of AdjacencyMatrix

        Returns:
            an array of size n representing the order in which
            nodes are visited (in a roundtrip)
    '''
    # Calculate the MST
    tree = mst(am)
    result = []
    # pre-order traversal on MST. Nodes listed.
    pre_order(tree, 0, result)
    return result


def mst(am):
    """Tests?"""
    # "Program testing can convincingly show the presence of bugs
    # but it is hopelessly inadequate to show their absence." EWD 340

    # STL
    n = am.node_size()

    def insert(heap, u, dist):
        return heapq.heappush(heap, (dist, u))

    def delete_min(heap):
        return heapq.heappop(heap)[1]

    # h := heap
    h = []
    # Distance array, ∞ for all nodes
    d = [math.inf for v in range(n)]
    # Node 0 as source
    d[0] = 0
    # Array storing marked ones
    marked = [False for v in range(n)]
    # Array storing the current parents
    parent = [None for v in range(n)]
    parent[0] = 0
    # Array at idx i containing the list of children of node i
    result_mst = [[] for v in range(n)]

    # Place all nodes to heap using distance as priority
    for u in range(n):
        insert(h, u, d[u])

    # While h is not empty
    while h:

        u = delete_min(h)

        if not marked[u]:
            # For all neighbors of u
            for v in range(n):
                w = am.get_weight(u, v)
                if not marked[v] and w < d[v] and v is not u:
                    d[v] = w
                    insert(h, v, d[v])
                    parent[v] = u
            marked[u] = True

            # Add edge {u, parent[u]} to the MST
            if u != 0:
                result_mst[parent[u]].append(u)

    return result_mst


def pre_order(tree, root, result):
    """Tests?"""

    result.append(root)

    for v in tree[root]:
        pre_order(tree, v, result)


def tour_weight(am, tour):
    '''
        computes the sum of edge weigths when all nodes of a
        tour are visited as a roundtrip

        Parameter:
            am - Instance of AdjacencyMatrix of size n
            tour - permuation of {0,...,n-1}

        Returns:
            the following value rounded to two decimal places
            w(tour[0],tour[1]) + ...
                           + w(tour[n-1],tour[n-1])
                           + w(tour[n-1],tour[0])
    '''
    n = am.node_size()
    weight_sum = 0

    for i in range(n-1):
        weight_sum += am.get_weight(tour[i], tour[i + 1])
    weight_sum += am.get_weight(tour[n-1], tour[0])

    return round(weight_sum, 2)


def read_graph_from_file(filename):
    '''
        reads a complete weighted graph from a file (that must
        be loated in same folder) and creates an adjacency matrix
        from it

        Parameter:
            filename - name of file

        Returns:
            instance of AdjacencyMatrix representing the file
    '''
    with open(filename) as input:
        lines = input.read().splitlines()
        # first line contains the number of nodes
        am = AdjacencyMatrix(int(lines[0]))

        # other lines contain edges seperated by a whitespace
        for i in range(0, len(lines) - 1):
            for j in range(am.node_size()):
                entries = lines[i + 1].split(' ')
                am.set_weight(i, j, float(entries[j]))

    return am


if __name__ == "__main__":
    am = read_graph_from_file('cities.txt')
    print("Computing Tour\n", compute_tour(am))
    print("Printing MST\n", mst(am))
