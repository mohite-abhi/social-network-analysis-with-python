import networkx as nx
import matplotlib.pyplot as plt


def set_all_B(G):
    for each in G.nodes():
        G.nodes[each]['action']='B'

def set_A(G,list1):
    for each in list1:
        G.nodes[str(each)]['action'] = 'A'

def get_colors(G):
    list1=[]
    for each in G.nodes():
        if G.nodes[each]['action']=='B':
            list1.append('red')
        else:
            list1.append('green')
    return list1    


def find_neigh(each,c,G):
    num=0
    for each1 in nx.neighbors(G,each):
        if G.nodes[each1]['action']==c:
            num=num+1
    return num

def recalculate_options(G):
    dict1 = {}
    a=3
    b=2
    for each in G.nodes():
        num_A = find_neigh(each,'A',G)
        num_B = find_neigh(each, 'B', G)
        payoff_A = a*num_A
        payoff_B = b*num_B
        if payoff_A>=payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each] = 'B'
    return dict1



def reset_node_attributes(G, action_dict):
    for each in action_dict:
        G.nodes[each]['action']=action_dict[each]


def terminate_1(c,G):
    f=1
    for each in G.nodes():
        if G.nodes[each]['action']!=c:
            f=0
            break
    return f




def terminate(G, count):
    flag1=terminate_1('A',G)
    flag2=terminate_1('B',G)
    if flag1==1 or flag2==1 or count>=100:
        return 1
    else:
        return 0

    