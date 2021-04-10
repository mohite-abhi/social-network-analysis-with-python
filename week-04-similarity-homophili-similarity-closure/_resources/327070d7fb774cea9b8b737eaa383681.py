import networkx as nx
import matplotlib.pyplot as plt


def no_of_obesity(G):
    num=0
    for each in G.nodes():
        if G.nodes[each]['name']==40:
            num+=1
    return num


def plot_time_vs_graph_data():
    x_time=[]
    y_density=[]
    y_obesity=[]
    for i in range(0,13):
        G=nx.read_gml('gml_network/evolution_{}.gml'.format(str(i)))
        x_time.append(i)
        y_density.append(nx.density(G))
        y_obesity.append(no_of_obesity(G))

    plt.xlabel('time')
    plt.ylabel('density')
    plt.title('delta density')
    plt.plot(x_time,y_density)
    plt.show()
    plt.plot(x_time,y_obesity)
    plt.show()


plot_time_vs_graph_data()