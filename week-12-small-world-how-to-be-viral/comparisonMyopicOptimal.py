from baseCode import *


def comparison(n):
    myopicPathLengths = []
    optimalPathLengths = []
    for i in range(n):
        myopicPathLengths.append(len(myopicSearch(G, H, i, i+n)))
        optimalPathLengths.append(len(nx.shortest_path(G, i,i+n)))

    xAxis = [i for i in range(n)]

    plt.plot(xAxis, myopicPathLengths, 'r')
    plt.plot(xAxis, optimalPathLengths, 'b')
    plt.show()

def main():
    G = makeRingGraph(100)
    H = G.copy()
    G = addLongLinks(G, 10)
    comparison(50)

    # colors = setPathColors(G, p, p1)
    # pos = nx.circular_layout(G)
    # nx.draw(G, node_color=colors, with_labels=True)
    # plt.show()

