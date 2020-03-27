#%%
file = open('../dataset/character.txt', 'r')
group = 1
# %%
for line in file:
    if line == '\n':
        group += 1
    else:
        line = line.strip('\n')
        _string = "{\"id\": \"" + line + "\", \"group\": " + str(group) + "},"
        print(_string)