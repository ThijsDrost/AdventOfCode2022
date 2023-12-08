loc = 'input.txt'
indexes = []
with open(loc, 'r') as file:
    for x, line in enumerate(file):
        for y, character in enumerate(line.removesuffix('\n')):
            if character == '#':
                indexes.append((x, y))


def step(indexes, num=0):
    rel_loc = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    directions = [[(-1, -1), (-1, 0), (-1, 1)], [(1, 1), (1, 0), (1, -1)], [(1, -1), (0, -1), (-1, -1)], [(-1, 1), (0, 1), (1, 1)]]
    directions[-num:], directions[:-num] = directions[:num], directions[num:]
    # print(directions)
    new_loc = []
    locs = set()
    moved = 0
    for index in indexes:
        for loc in rel_loc:
            if (index[0] + loc[0], index[1] + loc[1]) in indexes:
                break
        else:
            new_loc.append(index)
            continue
        for d in directions:
            for j in range(3):
                if (index[0]+d[j][0], index[1]+d[j][1]) in indexes:
                    # print(j)
                    break
            else:
                n_l = (index[0]+d[1][0], index[1]+d[1][1])
                if n_l not in locs:
                    # print(f'Walk {d[1]}')
                    locs.add(n_l)
                    new_loc.append(n_l)
                    moved += 1
                else:
                    new_loc.append(index)
                    for k, n in enumerate(new_loc):
                        if n == n_l:
                            new_loc[k] = indexes[k]
                            moved -= 1
                break
        else:
            new_loc.append(index)
    return new_loc, moved


def print_result(indexes):
    x_r = min(indexes, key=lambda x: x[0])[0], max(indexes, key=lambda x: x[0])[0]
    y_r = min(indexes, key=lambda y: y[1])[1], max(indexes, key=lambda y: y[1])[1]
    values = [['.' for _ in range(y_r[0], y_r[1]+1)] for _ in range(x_r[0], x_r[1]+1)]
    for index in indexes:
        values[index[0]-x_r[0]][index[1]-y_r[0]] = '#'
    print('\n'.join(' '.join(x) for x in values))
    print(f'Size is: {(x_r[1]-x_r[0]+1)*(y_r[1]-y_r[0]+1) - len(indexes)}')


print_result(indexes)
index = 0
while True:
    indexes, num = step(indexes, index % 4)
    # print(indexes)

    # print_result(indexes)

    if index == 9:
        print_result(indexes)
    print(index+1, num)
    if num == 0:
        break
    index += 1
    # print()
    # if num == 0:
    #     print('done')
# indexes = step(indexes, 1)
# print(indexes)
# print_result(indexes)

