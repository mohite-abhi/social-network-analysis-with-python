import networkx as nx
import random
import matplotlib.pyplot as plt
from math import log

def randomConnect(G, m):
    nodes = list(G.nodes())
    for i in range(int(m*log(m))):
        u = random.choice(nodes)
        v = random.choice(nodes)
        if u != v:
            G.add_edge(u,v)


def initiateBarbase(G,m0, n):
    # initialize the barbasi albert model
    G.add_nodes_from([1,2,3,4,5])
    randomConnect(G,m0)

    for u in range(6,n+1):
        distribution = [G.degree(i) for i in G.nodes()]
        distSum = sum(distribution)
        probability = [i/distSum for i in distribution]
        cumulativeProbability = [sum(probability[:i]) for i in range(1,(len(distribution)+1))]

        G.add_node(u)
        for i in range(1):
            randNo = random.random()
            v = cumulativeProbability.index(min(list(filter(lambda x: x>randNo,cumulativeProbability))))+1
            G.add_edge(u,v)

        pos = nx.circular_layout(G)
        nx.draw(G,pos,with_labels=True)
        plt.show()
    # print(G.edges())



def showDegDist(G):
    deg = [i[1] for i in nx.degree(G)]
    uniqDeg = list(set(deg))
    uniqDeg.sort()
    countDeg = [deg.count(i) for i in uniqDeg]
    plt.plot(uniqDeg,countDeg)
    plt.show()



G = nx.Graph()
initiateBarbase(G,m0=5,n=1000)
showDegDist(G)