import networkx as nx

def highest_between_edge(G):
    edge_betweenness_centrality = nx.edge_betweenness_centrality(G)
    edges_n_betweennesses = list(edge_betweenness_centrality.items())

    return max(edges_n_betweennesses, key=lambda x: x[1])[0]


def girvan_newman(G):
    connected_components = [i for i in nx.connected_components(G)]
    num_of_connected_components = len(connected_components)
    print('The number of connected components are : ',num_of_connected_components)

    while num_of_connected_components == 1:
        G.remove_edge(*highest_between_edge(G))
        connected_components = [i for i in nx.connected_components(G)]
        num_of_connected_components = len(connected_components)
        print('The number of connected components are : ',num_of_connected_components)

    return connected_components


# G = nx.barbell_graph(5,0)
# connected_components = girvan_newman(G)

# for i in connected_components:
#     print(i)
#     print('........')



G = nx.karate_club_graph()
connected_components = girvan_newman(G)

for i in connected_components:
    print(i)
    print('........')