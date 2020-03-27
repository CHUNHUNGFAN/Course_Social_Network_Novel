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

file3 = open("../dataset/network.csv",'r')
fileR = file3.readlines()

for row in fileR:
    row = row.strip().split(' ')
    G.add_edge(row[0],row[1], weight=1)

dicDegreeCentrality = nx.degree_centrality(G)
dicDegreeCentrality = {k: v for k, v in sorted(dicDegreeCentrality.items(), key=lambda item: item[1])}

labelStr = ""
valueStr = ""
for key, value in dicDegreeCentrality.items():
    labelStr = labelStr + "\"" + str(characters[int(key)]) + "\","
    valueStr = valueStr + str(value) + ","

print(labelStr)
print(valueStr)


# %%
