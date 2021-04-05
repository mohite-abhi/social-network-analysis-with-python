import networkx as nx
import itertools

def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()
    
    first_community = []
    for i in range(1,int(n/2+1)):
        comb = [list(x) for x in itertools.combinations(list(nodes),i)]
        first_community+=comb
    
    second_community = []
    for i in range(len(first_community)):
        l = list(set(nodes)-set(first_community[i]))
        second_community.append(l)
    

    # checking best combination which creates two communities
    # by finding which division has min inter community edges 
    # and max intra community edges
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = []

    for i in range(len(first_community)):
        G1_no_edges = G.subgraph(first_community[i]).number_of_edges()
        G2_no_edges = G.subgraph(second_community[i]).number_of_edges()
        num_intra_edges1.append(G1_no_edges)
        num_intra_edges2.append(G2_no_edges)
        G1_G2_inter_edges = G.number_of_edges() - G1_no_edges - G2_no_edges
        num_inter_edges.append(G1_G2_inter_edges)
        ratio.append((G1_no_edges+G2_no_edges)/G1_G2_inter_edges)

    max_index = ratio.index(max(ratio))
    print('( ',first_community[max_index],' ), ( ',second_community[max_index],' )')


G = nx.barbell_graph(5,0)
communities_brute(G)