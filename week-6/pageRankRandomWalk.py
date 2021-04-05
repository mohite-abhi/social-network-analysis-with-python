import networkx as nx
import random
import numpy as np

def add_edges(G,p):
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r<=p:
                    G.add_edge(i,j)
                else:
                    continue
    return G


def sort_nodes_by_points(points):
    points_array = np.array(points)
    sorted_args = np.argsort(-points_array)
    return sorted_args




def random_walk(G):
    nodes = list(G.nodes())
    points = [0 for i in range(G.number_of_nodes())]
    r = random.choice(nodes)
    points[r] += 1
    out = list(G.out_edges(r))

    for i in range(G.number_of_nodes()**3):
        if len(out) == 0:
            focus = random.choice(nodes)
        else:
            r1 = random.choice(out)
            focus = r1[1]
        points[focus]+= 1
        out = list(G.out_edges(focus))
    return points

def main():
    G=nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G=add_edges(G ,0.3)

    points = random_walk(G)

    sorted_nodes = sort_nodes_by_points(points)
    print(sorted_nodes)
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(),key=lambda x: x[1], reverse=True)
    for i in pr_sorted:
        print(i[0],end=" ")
main()