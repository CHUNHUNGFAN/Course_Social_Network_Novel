#%%
file = open("../dataset/novel.txt")

# %%
characters = []
file2 = open("../dataset/character.txt")
for line in file2:
    if line != '\n':
        line = line.strip('\n')
        characters.append(line)

# %%
relationship = [[0 for column in range(len(characters))] for row in range(len(characters))]
lines = file.readlines()
for line in lines:
    if line != '\n':
        links = []
        for index in range(len(characters)):
            if characters[index] in line:
                links.append(index)
        for row in range(len(links)):
            for column in range(row + 1, len(links)):
                relationship[links[row]][links[column]] += 1

# %%
charactersDegree=[0]*len(characters)
for row in range(len(characters)):
    for column in range(row + 1, len(characters)):
        if relationship[row][column] != 0:
            charactersDegree[row] += 1
            charactersDegree[column] += 1

# print(charactersDegree)

# %%
degree_dict = {i:charactersDegree.count(i) for i in charactersDegree}
degree_dict = {k: v for k, v in sorted(degree_dict.items(), key=lambda item: item[1])}
print(degree_dict)

#%%

# %%
labelStr = ""
valueStr = ""
for key, value in degree_dict.items():
    labelStr = labelStr + "\"" + str(key) + "\","
    valueStr = valueStr + str(value) + ","

print(labelStr)
print(valueStr)


# %%
