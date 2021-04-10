import networkx as nx
import matplotlib.pyplot as plt
import random


G=nx.Graph()
G.add_edges_from([
    (1,2),
    (3,11),
    (4,5),
    (5,6),
    (5,7),
    (5,8),
    (5,9),
    (5,10),
    (10,11),
    (10,13),
    (11,13),
    (12,14),
    (12,15),
    (13,14),
    (13,15),
    (13,16),
    (13,17),
    (14,15),
    (14,16),
    (15,16)
    ])




def independentCascade(G,seed):
    justInfected = list(seed)
    infected = list(seed)
    while 1:
        # print(justInfected, infected)
        if len(justInfected)==0:
            return infected
        temp = []
        for each in justInfected:
            for each1 in G.neighbors(each):
                rand = random.uniform(0,1)
                if rand < 0.5 and each1 not in infected and each1 not in temp:
                    temp.append(each1)
            infected += temp
            justInfected = list(temp)


# seed = [3,8]
# list1 = independentCascade(G,seed)