import re

def printer(mappert):
    print('\n'.join([' '.join(map('{0}'.format, m)) for m in mappert]))


lines = [line for line in open('input.txt', 'r').read().split('\n') if line]
mappert = [line.ljust(max(map(len, lines[:-1])), ' ') for line in lines[:-1]]
directions = lines[-1]
location = (0, mappert[0].index('.'))
rel_dir = (0, 1)
for num, direction in re.findall(r'(\d+)([A-Z])', directions):
    print(location)
    val = 0
    index = 1
    while val < int(num):
        match mappert[(location[0]+index*rel_dir[0]) % len(mappert)][(location[1]+index*rel_dir[1]) % len(mappert[0])]:
            case ' ':
                index += 1
            case '.':
                location = (location[0]+index*rel_dir[0]) % len(mappert), (location[1]+index*rel_dir[1]) % len(mappert[0])
                index = 1
                val += 1
            case '#':
                break
    if direction == 'R':
        rel_dir = rel_dir[1], -rel_dir[0]
    elif direction == 'L':
        rel_dir = -rel_dir[1], rel_dir[0]

total = 1000*(1+location[0]) + 4*(location[1]+1)
match rel_dir:
    case (0, 1):
        print(total + 0)
    case (0, -1):
        print(total + 2)
    case (1, 0):
        print(total + 3)
    case (-1, 0):
        print(total + 1)

# %%
lines = [line for line in open('test.txt', 'r').read().split('\n') if line]
mappert = [line.ljust(max(map(len, lines[:-1])), ' ') for line in lines[:-1]]
patch_size = 4
rotated = not (len(mappert)//patch_size == 4)
height = len(mappert)//patch_size
cube = {x: [] for x in range(6)}
for i, l in enumerate(((0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1))):
    if rotated:
        l = (l[1], l[0])
    if mappert[l[0]*patch_size][l[1]*patch_size] != ' ':
        cube[i] = [lin[patch_size*l[1]:patch_size*(l[1]+1)] for lin in mappert[patch_size*l[0]:patch_size*(l[0]+1)]]

for l, vals in zip(((0, 0), (0, 2), (2, 0), (2, 2), (3, 0), (3, 2)), ((0, 1), (0, 3), (1, 4), (3, 4), (1, 5), (3, 5))):
    if rotated:
        l = (l[1], l[0])
    if mappert[l[0]*patch_size][l[1]*patch_size] != ' ':
        if not cube[vals[0]]:
            cube[vals[0]] = [lin[patch_size*l[1]:patch_size*(l[1]+1)] for lin in mappert[patch_size*l[0]:patch_size*(l[0]+1)]]
        if not cube[vals[1]]:
            cube[vals[1]] = [lin[patch_size*l[1]:patch_size*(l[1]+1)] for lin in mappert[patch_size*l[0]:patch_size*(l[0]+1)]]
        if (not cube[vals[0]]) and (not cube[vals[1]]):
            raise ValueError()
for key, item in cube.items():
    print(key+1)
    printer(item)
    print()
# %%
patch_size = 4
lines = [line for line in open('test.txt', 'r').read().split('\n') if line]
mappert = [line.ljust(4*patch_size, ' ') for line in lines[:-1]]
mappert.extend([' '*4*patch_size for _ in range(4*patch_size - len(mappert))])


face = [[mappert[i*patch_size][j*patch_size] != ' ' for j in range(4)] for i in range(4)]
height = len(mappert)//patch_size
cube = {x: [] for x in range(1, 7)}

start = face[0].index(True)

loc_dict = {1: {'U': 4, "R": 3, "D": 2, "L": 5}, 2: {'U': 1, "R": 3, "D": 6, "L": 5}, 3: {'U': 1, "R": 4, "D": 6, "L": 2},
            4: {'U': 1, "R": 5, "D": 6, "L": 3}, 5: {'U': 1, "R": 2, "D": 6, "L": 4}, 6: {'U': 2, "R": 3, "D": 4, "L": 5}}


def make_cube(faces, mappert: list, location: tuple[int, int], rotation, been: set, cube: dict[int, list], cube_face: int):
    patch = [lin[patch_size * location[1]:patch_size * (location[1] + 1)] for lin in
                       mappert[patch_size * location[0]:patch_size * (location[0] + 1)]]
    for i in range(rotation % 4):
        patch = list(zip(*patch))[::-1]
    patch = [''.join(x) for x in patch]
    been.add(location)
    cube[cube_face] = patch
    print(location, cube_face, rotation)
    print(' ' + '\n '.join(patch))

    for loc, direction in zip(((1, 0), (0, 1), (-1, 0), (0, -1)), ('D', 'R', 'U', 'L')):
        new_loc = (location[0] + loc[0], location[1] + loc[1])
        if new_loc[0] == 4 or new_loc[1] == 4 or new_loc[0] == -1 or new_loc[1] == -1:
            continue
        if (faces[new_loc[0]][new_loc[1]]) and (new_loc not in been):
            if direction == 'L':
                rotation -= 1
            if direction == 'R':
                rotation += 1
            patch = [lin[patch_size*new_loc[1]:patch_size*(new_loc[1]+1)] for lin in mappert[patch_size*new_loc[0]:patch_size*(new_loc[0]+1)]]
            for i in range(rotation % 4):
                patch = list(zip(*patch))[::-1]
            make_cube(faces, mappert, new_loc, rotation, been, cube, cube_face=loc_dict[cube_face][direction])
    return cube


cube = make_cube(face, mappert, (0, start), 0, {(0, start)}, cube, 1)
