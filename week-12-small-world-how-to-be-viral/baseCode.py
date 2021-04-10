import networkx as nx
import matplotlib.pyplot as plt
import random



def makeRingGraph(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        G.add_edge(i%n, (i+1)%n)
        G.add_edge(i%n, (i+2)%n)
    return G


def addWeakTie(G):
    nodes = list(G.nodes())
    v1 = v2 = True
    while v1 == v2:
        v1 = random.choice(nodes)
        v2 = random.choice(nodes)
    G.add_edge(v1, v2)
    return G


def showGraph(G):
    pos = nx.circular_layout(G)
    nx.draw(G,pos)
    plt.show()



def addLongLinks(G, n, showPlot=False):
    x = [0]
    y = [nx.diameter(G)]
    for i in range(n):
        addWeakTie(G)
        x.append(i)
        y.append(nx.diameter(G))
    if showPlot:
        plt.xlabel('Number of weak ties added')
        plt.ylabel('Diameter')
        plt.plot(x,y)
        plt.show()
    return G



def findBestNeighbour(G, H, current, v):
    dis = G.number_of_nodes()
    for neighbour in G.neighbors(current):
        dis1 = len(nx.shortest_path(H, neighbour, v))
        if dis1 < dis:
            dis = dis1
            choice = neighbour
    return choice



def myopicSearch(G, H, u, v):
    path = [u]
    current = u
    while(1):
        w = findBestNeighbour(G, H, current, v)
        path.append(w)
        current=w
        if current == v:
            break
    return path



def setPathColors(G,p, p1):
    c =  []
    for each in G.nodes():
        if each == p[0]:
            c.append('red')
        elif each == p[len(p) - 1]:
            c.append('red')
        elif each in p:
            c.append('blue')
        elif each in p1:
            c.append('green')
        else:
            c.append('black')

    return c


def main():
    G = makeRingGraph(100)
    H = G.copy()
    G = addLongLinks(G, 10)
    p = myopicSearch(G, H, 0, 40)
    p1 = nx.shortest_path(G, 0,40)
    colors = setPathColors(G, p, p1)
    pos = nx.circular_layout(G)
    nx.draw(G, node_color=colors, with_labels=True)
    plt.show()
    # showGraph(G)

    #add long link

#main()