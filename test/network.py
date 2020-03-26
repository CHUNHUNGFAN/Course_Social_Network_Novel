#%%
import networkx as nx 

G = nx.Graph()

G.add_edge('A', 'B', weight=4)  
G.add_edge('B', 'D', weight=2)  
G.add_edge('A', 'C', weight=4)  
G.add_edge('C', 'D', weight=4)

print(nx.closeness_centrality(G))
# %%
