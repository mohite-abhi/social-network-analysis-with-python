import  networkx as nx
import matplotlib.pyplot as plt
import random
import itertools



def get_signs_of_triads(triadList,G):
    allSigns = []
    for i  in range(len(triadList)):
        temp=[]
        temp.append(G[triadList[i][0]][triadList[i][1]]['sign'])
        temp.append(G[triadList[i][1]][triadList[i][2]]['sign'])
        temp.append(G[triadList[i][0]][triadList[i][2]]['sign'])
        allSigns.append(temp)
    return allSigns


def count_unstable(all_signs):
    stable=0
    unstable=0
    for i in range(len(all_signs)):
        if all_signs[i].count('+')==3 or all_signs[i].count('+')==1:
            stable+=1
        if all_signs[i].count('+')==2 or all_signs[i].count('+')==0:
            unstable+=1
    return unstable


def move_triad_to_stable(G,triad_list,all_signs):
    found_unstable=False
    index=0
    while(found_unstable==False):
        index = random.randint(0,len(triad_list)-1)
        if all_signs[index].count('+') == 2 or all_signs[index].count('+') == 0:
            found_unstable=True

    r = random.randint(1,3)
    if all_signs[index].count('+') == 2:
        if r==1:
            if G[triad_list[index][0]][triad_list[index][1]]['sign']=='+':
                G[triad_list[index][0]][triad_list[index][1]]['sign']='-'
            elif G[triad_list[index][0]][triad_list[index][1]]['sign']=='-':
                G[triad_list[index][0]][triad_list[index][1]]['sign']='+'
        elif r==2:
            if G[triad_list[index][2]][triad_list[index][1]]['sign']=='+':
                G[triad_list[index][2]][triad_list[index][1]]['sign']='-'
            elif G[triad_list[index][2]][triad_list[index][1]]['sign']=='-':
                G[triad_list[index][2]][triad_list[index][1]]['sign']='+'
        elif r==3:
            if G[triad_list[index][0]][triad_list[index][2]]['sign']=='+':
                G[triad_list[index][0]][triad_list[index][2]]['sign']='-'
            elif G[triad_list[index][0]][triad_list[index][2]]['sign']=='-':
                G[triad_list[index][0]][triad_list[index][2]]['sign']='+'
    
    elif all_signs[index].count('+') == 0:
        if r==1:
            G[triad_list[index][0]][triad_list[index][1]]['sign']='+'
            
        elif r==2:
            G[triad_list[index][2]][triad_list[index][1]]['sign']='+'
            
        elif r==3:
            G[triad_list[index][0]][triad_list[index][2]]['sign']='+'
            
    return G



def see_coalitions(G):
    nodes=G.nodes()
    coalition1=list()
    coalition2=list()
    r=random.choice(list(G.nodes()))
    coalition1.append(r)



    processed_nodes=[]
    to_be_processed=[r]
    
    for each in to_be_processed:
        if each not in processed_nodes:
            neigh = list(G.neighbors(each))
            for i in range(len(neigh)):
                if G[each][neigh[i]]['sign']=='+':
                    if neigh[i] not in coalition1:
                        coalition1.append(neigh[i])
                    if neigh[i] not in to_be_processed:
                        to_be_processed.append(neigh[i])
                elif G[each][neigh[i]]['sign']=='-':
                    if neigh[i] not in coalition2:
                        coalition2.append(neigh[i])
                        processed_nodes.append(neigh[i])
            processed_nodes.append(node)

    return coalition1,coalition2

# create a graph with n nodes where nodes are the contries
G=nx.Graph()
n=8
G.add_nodes_from([i for i in range(1,n+1)])

mapping={1:'Afghanistan', 
   2:'Åland IslanX', 
   3:'Albania', 
   4:'Algeria', 
   5:'American SamS', 
   6:'AndorrA', 
   7:'Angola', 
   8:'Anguilla', 
   9:'Antarctica', 
   10:'Antigua', 
   11:'Argentina', 
   12:'Armenia', 
   13:'Aruba', 
   14:'Australia', 
   15:'Austria'}

G = nx.relabel_nodes(G,mapping)
#make it a complete graph

signs = ['+','-']
for i in G.nodes():
    for j in G.nodes():
        if i!=j:
            G.add_edge(i,j,sign=random.choice(signs))

edge_labels=nx.get_edge_attributes(G,'sign')
pos = nx.circular_layout(G)
nx.draw(G,pos,node_size=1000,with_labels=True,node_color='red')
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='red')

plt.show()



#get a list of all triads

#get list of triangle
node = G.nodes()
triad_list=[list(x) for x in itertools.combinations(node,3)]
#store signs of triads
all_signs=get_signs_of_triads(triad_list,G) #[['+','+'],[]]
#count number of untable triads
unstable=count_unstable(all_signs)

#make graph table
while(unstable!=0):
    G=move_triad_to_stable(G,triad_list,all_signs)
    all_signs=get_signs_of_triads(triad_list,G)
    unstable=count_unstable(all_signs)




first, second = see_coalitions(G)
print(first)
print(second)
pos = nx.circular_layout(G)
edge_labels=nx.get_edge_attributes(G,'sign')
nx.draw_networkx_nodes(G,pos,nodelist=first,node_color='red',node_size=1000,  alpha=0.8)
nx.draw_networkx_nodes(G,pos,nodelist=second,node_color='blue',node_size=1000,alpha=0.8)

nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_size=20,font_color='green')

plt.show()