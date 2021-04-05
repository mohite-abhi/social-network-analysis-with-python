import networkx as nx
import matplotlib.pyplot as plt
import random

N=10

def makeNeighbourGrid(N):
    G=nx.grid_2d_graph(N,N)
    for u,v in G.nodes():
        if u<N-1 and v<N-1:
            G.add_edge((u,v),(u+1,v+1))
            
    for u,v in G.nodes():
        if v>0 and u<N-1:
            G.add_edge((u,v),(u+1,v-1))

    for n in G.nodes():
        G.nodes[n]['type']=random.randint(0,2)
    return G

def returnTypeNodes(G,type1):
    return [n for (n,d) in G.nodes(data=True) if d['type']==type1]

def showGraph(G,N):

    gridPositions=dict((n,n) for n in G.nodes())
    labels=dict(((i,j),i*N+j)for i,j in G.nodes())

    empty_cells=returnTypeNodes(G,0)
    type1_node_list=returnTypeNodes(G,1)
    type2_node_list=returnTypeNodes(G,2)


    unsatisfiedNodesList = getUnsatisfiedNodesList(G,N)
    empty_cells=returnTypeNodes(G,0)
    type1_node_list=returnTypeNodes(G,1)
    type2_node_list=returnTypeNodes(G,2)

    nodes_g = nx.draw_networkx_nodes(G,gridPositions,node_color='green',nodelist=type1_node_list)
    nodes_r = nx.draw_networkx_nodes(G,gridPositions,node_color='red',nodelist=type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G,gridPositions,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G,gridPositions)
    nx.draw_networkx_labels(G,gridPositions,labels=labels)

    plt.show()

    empty_cells=returnTypeNodes(G,0)
    type1_node_list=returnTypeNodes(G,1)
    type2_node_list=returnTypeNodes(G,2)


    
    for i in range(1000):

        unsatisfiedNodesList = getUnsatisfiedNodesList(G,N)
        satisfyNode(unsatisfiedNodesList,empty_cells,labels)

        empty_cells=returnTypeNodes(G,0)
        type1_node_list=returnTypeNodes(G,1)
        type2_node_list=returnTypeNodes(G,2)

    nodes_g = nx.draw_networkx_nodes(G,gridPositions,node_color='green',nodelist=type1_node_list)
    nodes_r = nx.draw_networkx_nodes(G,gridPositions,node_color='red',nodelist=type2_node_list)
    nodes_w = nx.draw_networkx_nodes(G,gridPositions,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G,gridPositions)
    nx.draw_networkx_labels(G,gridPositions,labels=labels)
    plt.show()


# def getBoundaryNodes(G,N):
#     boundaryNodesList = list()
#     for (u,v),d in G.nodes(data=True):
#         if u==0 or u==N-1 or v==0 or v==N-1:
#             boundaryNodesList.append((u,v))
#     return boundaryNodesList
       

# def getNeighbours(u,v,N):
#     neighbours=[]
#     retList = []
#     for i in (-1,0,1):
#         for j in (-1,0,1):
#             if i!=0 or j!=0:
#                 neighbours.append((u+i,v+j))

#     for i in range(len(neighbours)):
#         if neighbours[i][0] < 0 or neighbours[i][0] > N-1 or neighbours[i][1] < 0 or neighbours[i][1] > N-1:
#             continue
#         retList.append(neighbours[i])
#     return retList


def satisfyNode(unsatisfiedNodesList, empty_cells, labels):
    if len(unsatisfiedNodesList) != 0:
        nodeToShift = random.choice(unsatisfiedNodesList)
        newPosition = random.choice(empty_cells)
        print(G.nodes[newPosition]['type'])
        G.nodes[newPosition]['type'] = G.nodes[nodeToShift]['type']
        G.nodes[nodeToShift]['type'] = 0
        labels[nodeToShift],labels[newPosition] = labels[newPosition],labels[nodeToShift]

def getUnsatisfiedNodesList(G,N):
    unsatisfiedNodesList = []
    t=3
    for u, v in G.nodes():
        type1 = G.nodes[(u,v)]['type']
        if type1 == 0:
            continue
        else:
            similarNodes = 0
            #neigh = getNeighbours(u,v,N)
            neigh=nx.neighbors(G,(u,v))
            for each in neigh:
                if G.nodes[each]['type']==type1:
                    similarNodes+=1
        if similarNodes <=t:
            unsatisfiedNodesList.append((u,v))
        
    return unsatisfiedNodesList



G=makeNeighbourGrid(10)
showGraph(G,10)

# boundaryNodesList = getBoundaryNodes(G,10)
# internalNodesList = list(set(G.nodes())-set(boundaryNodesList))
#print(internalNodesList)
# print(unsatisfiedNodesList)
#print(list(nx.neighbors(G,(0,0))))
