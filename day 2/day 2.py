loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 2\input.txt'

scores = {
    'A': {'X': 4, 'Y': 8, 'Z': 3},
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6}
}

score = 0
with open(loc, 'r') as file:
    for line in file:
        score += scores[line[0]][line[2]]
print(score)


# %%
shape = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
}
score = 0
with open(loc, 'r') as file:
    for line in file:
        score += scores[line[0]][shape[line[0]][line[2]]]
print(score)
