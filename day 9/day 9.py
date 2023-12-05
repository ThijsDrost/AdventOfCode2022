def solver(file_loc, num):
    been_set = {(0, 0)}
    body = [(0, 0) for _ in range(num)]
    direct_coord = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    with open(file_loc, 'r') as file:
        for j, line in enumerate(file):
            direction, distance = line.removesuffix('\n').split()
            for _ in range(int(distance)):
                body[0] = (body[0][0] + direct_coord[direction][0], body[0][1] + direct_coord[direction][1])

                for i in range(1, len(body)):
                    dx = body[i][0] - body[i-1][0]
                    dy = body[i][1] - body[i-1][1]
                    while abs(dx) > 1 or abs(dy) > 1:
                        if abs(dx) != 0:
                            body[i] = (body[i][0] - dx//abs(dx), body[i][1])
                        if abs(dy) != 0:
                            body[i] = (body[i][0], body[i][1] - dy//abs(dy))
                        dx = body[i][0] - body[i - 1][0]
                        dy = body[i][1] - body[i - 1][1]

                if body[-1] not in been_set:
                    been_set.add(body[-1])
    return len(been_set)


file_loc = 'input.txt'
print(solver(file_loc, 2))
print(solver(file_loc, 10))
