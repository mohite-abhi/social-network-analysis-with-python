import networkx as nx
import random

def createRandomGraph():
    G = nx.Graph()
    G.add_nodes_from([i for i in range(100)])
    nodes = list(G.nodes())
    for i in range(500):
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            G.add_edge(u,v)
    return G
