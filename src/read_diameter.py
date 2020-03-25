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
for row in range(len(characters)):
    for column in range(row + 1, len(characters)):
        if relationship[row][column] != 0:
            # _string = "{\"source\": \"" + str(characters[row]) + "\", \"target\": \"" + str(characters[column]) + "\", \"value\": " + str(relationship[row][column]) + "},"
            _string = str(row) + " " + str(column)
            print(_string)

# %%
