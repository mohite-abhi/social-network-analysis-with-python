import networkx as nx
import random
from matplotlib import pyplot as plt
import numpy

def add_nodes(n):
    '''
    add n number of nodes in graph and return it
    '''
    G=nx.Graph()
    G.add_nodes_from(range(n))
    return G


def add_random_edge(G):
    '''
    add one random edge
    '''
    v1 = random.choice(list(G.nodes()))
    v2 = random.choice(list(G.nodes()))

    if v1 != v2:
        G.add_edge(v1,v2)
    
    return G

def add_till_connedted(G):
    '''
    keeps adding edges in graph till it is connected
    '''
    while(nx.is_connected(G) == False):
        G=add_random_edge(G)
    return G


def minEdgeToConnectNodes(n):
    '''
    takes number of nodes and returns min. no. of edges selected at random taken to connect the graph of n nodes
    '''
    G=add_nodes(n)
    G=add_till_connedted(G)
    return G.number_of_edges()



def plotMinEdgeToConnect():
    '''
    plot the graph bw no. of edges taken to connect graph of n nodes VS no of nodes
    '''
    xAxis=[]
    yAxis=[]
    yAxisNotAvg=[]
    noOfNodes=10

    while(noOfNodes <= 400):
        
        summationEdgesToConnect=0

        for i in range(100):
            edgesToConnect = minEdgeToConnectNodes(noOfNodes)
            if summationEdgesToConnect == 0:
                yAxisNotAvg.append(edgesToConnect)
            summationEdgesToConnect += edgesToConnect

        avgEdgesToConnect = summationEdgesToConnect/100
        
        xAxis.append(noOfNodes)
        yAxis.append(avgEdgesToConnect)
        
        noOfNodes+=10

    plt.plot(xAxis,yAxis)
    plt.plot(xAxis,yAxisNotAvg)
    plt.xlabel("no. of nodes")
    plt.ylabel("avg. no of edges to connect graph")
    plt.title("Emergence of connectivity")

    x1=[]
    y1=[]
    i=10
    while(i<=400):
        x1.append(i)
        y1.append(i*numpy.log(i)*0.5)
        i+=10
    plt.plot(x1,y1)
    plt.show()