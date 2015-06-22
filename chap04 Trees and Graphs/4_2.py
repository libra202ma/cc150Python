"""
Given a directed graph, design an algorithm to find out whether
there is a route between two nodes.

- search. Start the search from one node, using DFS / BFS to see if
the other node can be found. Be careful about loops in the graph.

Trade-offs between DFS and BFS. For BFS, it could found shortest path,
while DFS could be implemented using simple recursions.
"""


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'stacks_and_queues'))

from queue import Queue


def findrouteDFS(graph, source, target, visited={}):
    if source == target:
        return True
    else:
        visited[source] = 1

    for e in source.neighbours and e not in visited:
        findrouteDFS(graph, e, target, visited)


def findrouteBFS(graph, source, target):
    v = {}  # visited nodes
    q = []  # to be checked nodes
    v[source] = True
    q.enqueue(source)
    while q:
        n = q.dequeue()
        if n == target:
            return True
        for e in n.neighbours and e not in v:
            v[e] = True
            q.enqueue(e)
