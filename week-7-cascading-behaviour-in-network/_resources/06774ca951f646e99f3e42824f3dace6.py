import networkx as nx
import random
from diffusion import *
import matplotlib.pylab as plt
G=nx.Graph()

G.add_edges_from([
    ('0', '1'),
    ('0', '6'),
    ('1', '2'),
    ('1', '8'),
    ('1', '12'),
    ('2', '9'),
    ('2', '12'),
    ('3', '4'),
    ('3', '9'),
    ('3', '3'),
    ('4', '5'),
    ('4', '12'),
    ('5', '6'),
    ('5', '10'),
    ('6', '8'),
    ('7', '8'),
    ('7', '9'),
    ('7', '10'),
    ('7', '11'),
    ('8', '9'),
    ('8', '10'),
    ('8', '11'),
    ('9', '10'),
    ('9', '11'),
    ('10', '11')])
    

list2 = [[i for i in range(5)],[0,2,3,4],[i for i in range(1,5)],[i for i in range(2,6)],[i for i in range(3,7)],
[4,5,6,12],[2,3,4,12],[i for i in range(6)],[i for i in range(6)]+[12]]

for list1 in list2:
    print(list1)
    set_all_B(G)
    set_A(G, list1)

    flag=0
    count=0
    while(1):
        flag = terminate(G,count)
        if flag==1:
            break
        count+=1
        action_dict = recalculate_options(G)
        reset_node_attributes(G, action_dict)
        colors = get_colors(G)

    c=terminate_1('A',G)
    if c==1:
        print("cascade complete")
    else:
        print("cascade incomplete")
    nx.draw(G, node_color=colors, node_size=800, with_labels=True)
    plt.show()