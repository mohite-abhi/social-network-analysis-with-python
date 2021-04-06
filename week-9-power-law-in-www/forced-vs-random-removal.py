import networkx as nx
import matplotlib.pyplot as plt
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

def removeRandomNode(G):
    nodes = list(G.nodes())
    r = random.choice(nodes)
    G.remove_node(r)
    return G

def removeSelectiveNode(G):
    degrees = G.degree()
    max = -1
    val = -1
    for i in degrees:
        if i[1] > max:
            max = i[1]
            val = i[0]
    G.remove_node(val)
    return G

def main():
    G = createRandomGraph()
    print("=====random removal======")
    G1 = G.copy()
    nodes_removed_random=0

    while(nx.is_connected(G1)):
        G1 = removeRandomNode(G1)
        nodes_removed_random += 1

    print("nodes removed when chosen randomly : ",nodes_removed_random)

    print()
    print()
    print()
    print()

    print("=====selective removal======")
    G2 = G.copy()
    nodes_removed_selective=0

    while(nx.is_connected(G2)):
        G2 = removeSelectiveNode(G2)
        nodes_removed_selective += 1

    print("nodes removed when chosen selectively : ",nodes_removed_selective)



main()