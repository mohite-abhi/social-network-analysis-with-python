from cascadeModel import independentCascade, G, nx
import numpy as np

dict_deg = dict(G.degree())
dict_cl=nx.closeness_centrality(G)
dict_cr=nx.core_number(G)
dict_bw = nx.betweenness_centrality(G)

dict_cascade={}
for each in G.nodes():
    c=[]
    for num in range(0,1000):
        seed=[each]
        i = independentCascade(G,seed)
        c.append(len(i))
    dict_cascade[each] = np.average(c)


sorted_dict_cascade=sorted(dict_cascade,key=dict_cascade.get,reverse=True)
sorted_dict_deg=sorted(dict_deg,key=dict_deg.get,reverse=True)
sorted_dict_cl=sorted(dict_cl,key=dict_cl.get,reverse=True)
sorted_dict_bw=sorted(dict_bw,key=dict_bw.get,reverse=True)
sorted_dict_cr=sorted(dict_cr,key=dict_cr.get,reverse=True)



print(sorted_dict_deg)
print(sorted_dict_cl)
print(sorted_dict_bw)
print(sorted_dict_cr)
print(sorted_dict_cascade)