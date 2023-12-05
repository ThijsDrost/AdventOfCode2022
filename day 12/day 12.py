from dataclasses import dataclass
from copy import deepcopy
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y, g, target, path: list):
        self.x = x
        self.y = y
        self.g = g
        self.h = (target[0] - x)**2 + (target[1] - y)**2
        self.path = path + [(x, y)]

    @property
    def f(self):
        return self.g + self.h

    def __repr__(self):
        return f'x:{self.x}, y:{self.y}, g:{self.g}, h:{self.h}'


def letter_value(letter):
    if letter.isupper():
        if letter == 'S':
            return letter_value('a')
        elif letter == 'E':
            return letter_value('z')
    else:
        return ord(letter) - 96


def read_map(loc):
    with open(loc, 'r') as file:
        mapper = []
        for i, line in enumerate(file):
            line = line.removesuffix('\n')
            mapper.append(list(map(letter_value, line)))
            if line.find('S') != -1:
                start = (line.find('S'), i)
            if line.find('E') != -1:
                end = (line.find('E'), i)

    return start, end, mapper


def show_path(mappert, node):
    for loc in node.path:
        mappert[loc[1]][loc[0]] = 0

    res = []
    for line in mappert:
        res.append(' '.join(map(str, line)))
    plt.figure()
    plt.imshow(mappert)
    plt.show()
    # print('\n'.join(res))


# %%
start_loc, target_loc, mappert = read_map('input.txt')

nodes = [Node(start_loc[0], start_loc[1], 0, target_loc, [])]
mappert2 = deepcopy(mappert)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
done = set()


steps = 0
while nodes:
    steps += 1
    node = nodes.pop(0)

    if node.x == target_loc[0] and node.y == target_loc[1]:
        print(f'Found target after {node.g} steps')
        break

    if node.y + 1 != len(mappert) and (node.x, node.y+1) not in done:
        if mappert[node.y][node.x] - mappert[node.y + 1][node.x] >= -1:
            nodes.append(Node(node.x, node.y + 1, node.g + 1, target_loc, node.path))
            done.add((node.x, node.y+1))
    if node.y - 1 != -1 and (node.x, node.y-1) not in done:
        if mappert[node.y][node.x] - mappert[node.y - 1][node.x] >= -1:
            nodes.append(Node(node.x, node.y - 1, node.g + 1, target_loc, node.path))
            done.add((node.x, node.y-1))
    if node.x + 1 != len(mappert[0]) and (node.x+1, node.y) not in done:
        if mappert[node.y][node.x] - mappert[node.y][node.x + 1] >= -1:
            nodes.append(Node(node.x + 1, node.y, node.g + 1, target_loc, node.path))
            done.add((node.x+1, node.y))
    if node.x - 1 != -1 and (node.x-1, node.y) not in done:
        if mappert[node.y][node.x] - mappert[node.y][node.x - 1] >= -1:
            nodes.append(Node(node.x - 1, node.y, node.g + 1, target_loc, node.path))
            done.add((node.x-1, node.y))
    mappert2[node.y][node.x] = -1
    # nodes.sort(key=lambda x: x.f, reverse=False)
else:
    print('no path found')
print(steps)
print(len(mappert)*len(mappert[0]))

# %%
min_val = 1000
for i in range(len(mappert)):
    nodes = [Node(start_loc[0], i, 0, target_loc, [])]
    mappert2 = deepcopy(mappert)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    done = set()

    steps = 0
    while nodes:
        steps += 1
        node = nodes.pop(0)

        if node.x == target_loc[0] and node.y == target_loc[1]:
            print(f'Found target after {node.g} steps')
            break

        if node.y + 1 != len(mappert) and (node.x, node.y + 1) not in done:
            if mappert[node.y][node.x] - mappert[node.y + 1][node.x] >= -1:
                nodes.append(Node(node.x, node.y + 1, node.g + 1, target_loc, node.path))
                done.add((node.x, node.y + 1))
        if node.y - 1 != -1 and (node.x, node.y - 1) not in done:
            if mappert[node.y][node.x] - mappert[node.y - 1][node.x] >= -1:
                nodes.append(Node(node.x, node.y - 1, node.g + 1, target_loc, node.path))
                done.add((node.x, node.y - 1))
        if node.x + 1 != len(mappert[0]) and (node.x + 1, node.y) not in done:
            if mappert[node.y][node.x] - mappert[node.y][node.x + 1] >= -1:
                nodes.append(Node(node.x + 1, node.y, node.g + 1, target_loc, node.path))
                done.add((node.x + 1, node.y))
        if node.x - 1 != -1 and (node.x - 1, node.y) not in done:
            if mappert[node.y][node.x] - mappert[node.y][node.x - 1] >= -1:
                nodes.append(Node(node.x - 1, node.y, node.g + 1, target_loc, node.path))
                done.add((node.x - 1, node.y))
        mappert2[node.y][node.x] = -1
        # nodes.sort(key=lambda x: x.f, reverse=False)
    else:
        print('no path found')
    if node.g < min_val:
        min_val = node.g
print(min_val)
