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
charactersLinks = [[] for row in range(len(characters))]
for row in range(len(characters)):
    temp = []
    for column in range(row + 1, len(characters)):
        if relationship[row][column] != 0:
            charactersLinks[row].append(column)
            charactersLinks[column].append(row)

#%%
charactersTriangles = [0]*len(characters)
for row in range(len(characters)):
    rowLinks = charactersLinks[row]
    for column in range(len(rowLinks)):
        columnLinks = charactersLinks[rowLinks[column]]
        charactersTriangles[row]+= len(set(rowLinks).intersection(columnLinks))

charactersTriangles = [int(number / 2) for number in charactersTriangles]

# %%
charactersCI = [0]*len(characters)
sumCI = 0
for character in range(len(characters)):
    if len(charactersLinks[character]) != 1:
        charactersCI[character] = charactersTriangles[character] / ((len(charactersLinks[character]) * (len(charactersLinks[character]) - 1)) / 2)
        sumCI += charactersCI[character]

averageCI = sumCI / len(charactersCI)
print(averageCI)
#%%
