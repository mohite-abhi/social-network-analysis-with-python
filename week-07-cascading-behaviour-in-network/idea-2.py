from diffusion import *

G = nx.read_gml('random_graph.gml')

for u in G.nodes():
    for v in G.nodes():
        if u<v:
            print(u,v,' : ')
            list1=[]
            list1.append(u)
            list1.append(v)


            set_all_B(G)

            set_A(G, list1)
            colors = get_colors(G)
            # nx.draw(G, node_color=colors, node_size=800, with_labels=True)
            # plt.show()

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
            # nx.draw(G, node_color=colors, node_size=800, with_labels=True)
            # plt.show()