import networkx as nx
import matplotlib.pyplot as plt

#G=nx.read_edgelist('datasets/facebook_combined.txt')
#G=nx.read_pajek('datasets/football.net')
#G = nx.read_graphml('dataset/manhatten.graphml')
#G = nx.read_gexf('datasets/diseasome.gexf')
G = nx.read_gml('datasets/karate.gml', label = 'id')
#print(nx.info(G))

#print(nx.number_of_nodes(G))
#print(nx.number_of_edges(G))
#print(nx.is_directed(G))

#nx.draw(G)
'''
def plot_deg_dist(G):
    all_degrees = list(dict(nx.degree(G)).values())
    unique_digrees = list(set(all_degrees))

    count_of_degrees = list()
    for i in unique_digrees:
        x = all_degrees.count(i)
        count_of_degrees.append(x)

    plt.loglog(unique_digrees, count_of_degrees, 'go-')
    plt.xlabel('Degrees')
    plt.ylabel('Number of nodes')
    plt.title('Degree distribution of karate network')
    plt.show()
'''
#nx.draw_circular(G)
#plt.show()

#plot_deg_dist(G)

#print("Density is ",nx.density(G))

#nx.clustering(G)

'''
for i in nx.clustering(G).items():
    print(i)
'''
#print(nx.average_clustering(G))

print("diameter is ",nx.diameter(G))