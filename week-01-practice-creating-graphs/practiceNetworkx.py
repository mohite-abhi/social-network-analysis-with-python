# coding: utf-8
import networkx
# G=networkxGraph()
G=networkx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.nodes()
G.add_node(6)
G.nodes()
G.add_edges(1,2)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(4,6)
G.add_edge(5,4)
G.add_edge(2,3)
G.edges()
G.add_edge(2,6)
import networkx as nx
G.nodes()
G.edges()
import matplotlib.pyplot as plt
nx.draw(G)
plt.show()
nx.draw(G, with_lables=1)
nx.draw(G, with_labels=1)
plt.show()
Z = nx.complete_graph(10)
Z.nodes()
print (Z.nodes())
print (Z.edges())
Z.order()
Z.size()
nx.draw(Z,with_labels=1)
plt.show()
H=nx.complete_graph(100)
nx.draw(H)
plt.show()
G=nx.gnp_random_graph(20,0.5)
nx.draw(G)
plt.show()
plt.show()
plt.show()
nx.draw(G)
plt.show()
G=nx.gnp_random_graph(5,0.5)
nx.draw(G)
plt.show()
nx.draw(G)
plt.show()
nx.draw(G)
plt.show()
G=nx.gnp_random_graph(5,0.9)
nx.draw(G)
plt.show()
G = nx.DiGraph()
nx.draw(G)
plt.show()
city_set = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur']
city_set
city_set
for i in city_set:
        G.add_node(i)
        
G.nodes()
# nx.draw()
plt.show()
nx.draw(G)
plt.show()
nx.draw(G,show_labels=1)
nx.draw(G,show_label=1)
nx.draw(G)
plt.show()
nx.draw(G,with_label=1)
nx.draw(G,with_labels=1)
plt.show()
costs=[]
for i in range(1,21):
        costs.append(i*100)
        
costs
import random
random.choice([1,2,3,4,5])
random.choice([1,2,3,4,5])
while(G.number_of_edges()<16):
    c1=random.choice(G.nodes())
    c2=random.choice(G.nodes())
    if c1!=c2 and G.has_edges(c1,c2)==0:
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
        
        
G.nodes()
random.choice(G.nodes())
random.choice([1,2,3,4,5])
# random.choice()
list(G.nodes())
while(G.number_of_edges()<16):
    c1=random.choice(list(G.nodes()))
    c2=random.choice((G.nodes()))
    if c1!=c2 and G.has_edges(c1,c2)==0:
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
        
        
while(G.number_of_edges()<16):
    c1=random.choice(list(G.nodes()))
    c2=random.choice(list(G.nodes()))
    if c1!=c2 and G.has_edges(c1,c2)==0:
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
        
        
while(G.number_of_edges()<16):
    c1=random.choice(list(G.nodes()))
    c2=random.choice(list(G.nodes()))
    if c1!=c2 and G.has_edge(c1,c2)==0:
        w=random.choice(costs)
        G.add_edge(c1,c2,weight=w)
        
        
G.edges()
nx.draw(G,with_labels=1)
plt.show()
pos=nx.spectral_layout(G)
nx.draw(pos,with_labels=1)
# pos=nx.spectral_layout(G,with_labels=1)
pos=nx.spectral_layout(G)
nx.draw(pos)
nx.draw(G,pos)
plt.show()
G.nodes()
G.edges()
pos=nx.spectral_layout(G)
pos
nx.draw(pos)
plt.show()
plt.show()
nx.draw(G ,pos)
plt.show()
nx.draw(G ,pos)
plt.show()
pos=nx.circular_layout(G)
nx.draw(G,pos)
plt.show()
nx.draw(G,pos,with_labels=1)
nx.draw(G,pos,with_labels=1)
plt.show()
# nx.draw_networkx_edge_labels(G,pos,with_labels=1)
nx.draw_networkx_edge_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos)
plt.show()
# nx.draw_networkx_edge_labels(G)
nx.draw(G)
nx.draw_networkx_edge_labels(G,pos)
plt.show()
nx.is_connected(G)
# get_ipython().run_line_magic('s', 'current_session ~0/')
# get_ipython().run_line_magic('save', 'current_session ~0/')
plt.show()
nx
import networkx as nx
nx.is_connected(G)
G
G.nodes()
G.edges()
nx.is_connected(G)
# get_ipython().run_line_magic('save', 'current_session ~0/')
