import matplotlib.pyplot as plt
import networkx as nx
import grafos as Gr
import vertice as v

def desenhar(K: Gr.grafo): 
    G = nx.Graph()
    color_map = []
    for i in K.vertices:
        G.add_node(i.nome)
        color_map.append(i.color)
    
    for i in K.arestas:
        x, y = i
        G.add_edge(K.vertices[x].nome, K.vertices[y].nome, weight=K.mat_custos[x][y])

    base_options = {"node_size": 200}

    subax1 = plt.subplot(121)
    pos = nx.spring_layout(G, 4)
    nx.draw_networkx(G,pos = pos, node_color=color_map, with_labels = True)


    subax2 = plt.subplot(122)
    pos = nx.spring_layout(G, 4)
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color= "Gray")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}, **base_options
    )

    plt.suptitle("Grafo básico: Exibições \n Cor/Peso")
    plt.tight_layout()
    plt.show()