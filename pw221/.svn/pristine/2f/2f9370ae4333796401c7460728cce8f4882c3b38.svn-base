"""
Functions for scheduling jobs on machines

Copyright 2020, University of Freiburg

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""

import queue

from AdjacencyList import AdjacencyList


def dispatch_sequence(al: AdjacencyList):
    '''
        computes a valid sequence in which jobs can be
        dispatched to a single machine without violating
        the depency graph given as parameter

        Parameter:
            al - depency graph as instance of AdjacencyList

        Returns:
            a list representing a valid sequence of IDs for
            computing the respective jobs on a single machine
            or None if such a sequence does not exist

        Unit Tests (leave this one, but add more):
            >>> from AdjacencyList import AdjacencyList
            >>> cycle = AdjacencyList(6)
            >>> cycle.add_edge(0,1); cycle.add_edge(1,2)
            >>> cycle.add_edge(2,3); cycle.add_edge(3,0)
            >>> cycle.add_edge(4,5);
            >>> dispatch_sequence(cycle) is None
            True
    '''
    def dfs(al: AdjacencyList, start: int, visited=None):
        if visited is None:
            visited = []
        visited.append(start)
        for element in al.get_neighbors(start):
            if element not in visited:
                dfs(al, element, visited)
        return visited

    def dfs_(al: AdjacencyList, start, discovered, departure, time):
        discovered[start] = True
        for i in al.edges[start]:
            if not discovered[i]:
                time = dfs_(al, i, discovered, departure, time)
        departure[start] = time
        time = time + 1
        return time

    def is_dag(al: AdjacencyList):
        discovered = [False] * al.node_size()
        departure = [None] * al.node_size()
        time = 0
        for i in range(al.node_size()):
            if not discovered[i]:
                time = dfs_(al, i, discovered, departure, time)
        for j in range(al.node_size()):
            for k in al.edges[j]:
                if departure[j] <= departure[k]:
                    return False
        return True

    if is_dag(al) is False:
        return None
    else:
        return dfs(al, 0, visited=None)


def earliest_computation(al: AdjacencyList):
    '''
        for each job, gives the earliest point in time it can
        be completed, which is when at least one parent in the
        depency graph has been computed or it has indegree 0.

        Parameter:
            al - depency graph as instance of AdjacencyList

        Returns:
            a list of size n containing at position i the
            earliest point in time it can be computed
    '''
    earliest = [0 for v in range(al.node_size())]
    roots = al.get_roots()

    # BFS
    for root in roots:
        q = queue.SimpleQueue()
        q.put(root)
        while not q.empty():
            u = q.get()
            for v in al.get_neighbors(u):
                earliest[v] = earliest[u] + 1
                q.put(v)
    return earliest


def read_graph_from_file(filename):
    '''
        reads a depency graph from a file (that must be loated
        in same folder) and creates an adjacency list from it

        Parameter:
            filename - name of file

        Returns:
            instance of AdjacencyList representing the file
    '''
    with open(filename) as input:
        lines = input.read().splitlines()
        # first line contains the number of nodes
        al = AdjacencyList(int(lines[0]))

        # other lines contain edges seperated by a whitespace
        for i in range(1, len(lines)):
            source = int(lines[i].split(' ')[0])
            target = int(lines[i].split(' ')[1])
            al.add_edge(source, target)

    return al


# if __name__ == "__main__":
#     AL = read_graph_from_file('dag.txt')
#     print(dispatch_sequence(AL))
#     print("Begin of List")
#     print(earliest_computation(AL))
#     print("End of List")
