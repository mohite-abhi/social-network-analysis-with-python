import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import time

def create_graph_with_nodes(n):
    G=nx.Graph()
    #G.add_nodes_from(range(1,101))
    for i in range(1,n+1):
        G.add_node(i)
    return G
    

def render_graph_for(G, t=0):
    time.sleep(1)
    label_dict = get_labels(G)
    node_size = get_size(G)
    color_array = get_colors(G)
    nx.draw(G,labels = label_dict, node_size=node_size, node_color=color_array)
    plt.savefig('evolution.jpg')
    plt.clf()
    plt.cla()
    nx.write_gml(G, 'gml_network/evolution_{}.gml'.format(str(t)))



def assign_bmi_to_graph(G):
    for i in G.nodes():
        G.nodes[i]['name'] = random.randint(15,40)
        G.nodes[i]['type'] = 'person'


def get_labels(G):
    dict1 = {}
    for i in G.nodes():
        dict1[i]=G.nodes[i]['name']
    return dict1


def get_size(G):
    sizeArray = []
    for i in G.nodes():
        if G.nodes[i]['type']=='person':
            sizeArray.append(G.nodes[i]['name']*20)
        else:
            sizeArray.append(2000)
    return sizeArray


def add_foci_nodes(G):
    n=G.number_of_nodes()
    i=n+1
    foci_nodes = ['gym', 'eatout', 'movie_club', 'karate_club', 'yoga_club']
    for j in range(5):
        G.add_node(i)
        G.nodes[i]['name']=foci_nodes[j]
        G.nodes[i]['type']='foci'
        i+=1


def get_colors(G):
    colorList=[]
    for i in G.nodes():
        if G.nodes[i]['type']=='person':
            if G.nodes[i]['name']==15:
                colorList.append('green')
            elif G.nodes[i]['name']==40:
                colorList.append('yellow')
            else:
                colorList.append('blue')
        else:
            colorList.append('red')
    return colorList



def get_foci_not_person_nodes(really=True):
    nodes=[]
    for i in G.nodes():
        if really:
            if G.nodes[i]['type']=='foci':
                nodes.append(i)
        else:
            if G.nodes[i]['type']=='person':
                nodes.append(i)
    return nodes



def add_foci_edges():
    foci_nodes=get_foci_not_person_nodes(True)
    person_nodes=get_foci_not_person_nodes(False)
    for i in person_nodes:
        r=random.choice(foci_nodes)
        G.add_edge(i,r)



def homophily(G):
    person_nodes=get_foci_not_person_nodes(False)
    for u in person_nodes:
        for v in person_nodes:
            if u!=v:
                dif_in_bmi = abs(G.nodes[u]['name']-G.nodes[v]['name'])
                probConnection = float(1)/(dif_in_bmi+1000)
                randomDec=random.uniform(0,1)
                if randomDec<probConnection:
                    G.add_edge(u,v)


def noCommonNeighbour(u,v,G):
    noNeighbourU = set(G.neighbors(u))
    noNeighbourV = set(G.neighbors(v))
    return len(noNeighbourU & noNeighbourV)



def closure(G):
    array1 = []
    for u in G.nodes():
        for v in G.nodes():
            if u!= v and (G.nodes[u]['type']=='person' or G.nodes[v]['type']=='person'):
                k=noCommonNeighbour(u,v,G)
                p = 1-math.pow((1-0.01),k)
                tmp=[]
                tmp.append(u)
                tmp.append(v)
                tmp.append(p)
                array1.append(tmp)
    for entry in array1:
        u=entry[0]
        v=entry[1]
        p=entry[2]

        r = random.uniform(0,1)
        if r<p:
            G.add_edge(u,v)



def change_bmi(G):
    fnodes=get_foci_not_person_nodes()
    for each in fnodes:
        if G.nodes[each]['name']=='eatout':
            for each1 in G.neighbors(each):
                if G.nodes[each1]['name']!=40:
                    G.nodes[each1]['name']+=1
        if G.nodes[each]['name']=='gym':
            for each1 in G.neighbors(each):
                if G.nodes[each1]['name']!=15:
                    G.nodes[each1]['name']-=1



G=create_graph_with_nodes(100)
assign_bmi_to_graph(G)
add_foci_nodes(G)
add_foci_edges()

time.sleep(3)
render_graph_for(G)

for t in range(12):
    homophily(G)
    closure(G)
    change_bmi(G)
    render_graph_for(G,t+1)
