#%%
import networkx as nx 
file = open("../dataset/novel.txt")

characters = []
file2 = open("../dataset/character.txt")
for line in file2:
    if line != '\n':
        line = line.strip('\n')
        characters.append(line)

G = nx.Graph()

file = open("../dataset/network.csv",'r')
fileR = file.readlines()

for row in fileR:
    row = row.strip().split(' ')
    G.add_edge(row[0],row[1], weight=1)

dicClosenessCentrality = nx.closeness_centrality(G)
dicClosenessCentrality = {k: v for k, v in sorted(dicClosenessCentrality.items(), key=lambda item: item[1])}

labelStr = ""
valueStr = ""
for key, value in dicClosenessCentrality.items():
    labelStr = labelStr + "\"" + str(characters[int(key)]) + "\","
    valueStr = valueStr + str(value) + ","

print(labelStr)
print(valueStr)


# %%
