import matplotlib.pyplot as plt

loc = 'input.txt'
total_coords = []
with open(loc, 'r') as file:
    lines = [line.removesuffix('\n') for line in file]
for x in lines:
    if x == '\n':
        break
    total_coords.append(list(map(lambda y: list(map(int, y.split(','))), x.split('->'))))

y_range = [0, 0]
for line in total_coords:
    for coord in line:
        y_range[0] = min(y_range[0], coord[1])
        y_range[1] = max(y_range[1], coord[1])
y_range[1] += 1
x_range = [500-y_range[1], 500+y_range[1]]

mappert = [['.' for _ in range(x_range[1]-x_range[0]+1)] for _ in range(y_range[1]-y_range[0]+1)]
for i in range(len(total_coords)):
    for j in range(1, len(total_coords[i])):
        for x in range(min(total_coords[i][j-1][0], total_coords[i][j][0]), max(total_coords[i][j-1][0], total_coords[i][j][0])+1):
            for y in range(min(total_coords[i][j-1][1], total_coords[i][j][1]), max(total_coords[i][j-1][1], total_coords[i][j][1])+1):
                mappert[y-y_range[0]][x-x_range[0]] = '#'


# print('\n'.join([' '.join(m) for m in mappert]))
sand = 500, 0
num = 0
uno = False
while True:
    # if not (y_range[0] <= sand[1] <= y_range[1] and x_range[0] <= sand[0] <= x_range[1]):
    #     break
    if mappert[0-y_range[0]][500-x_range[0]] == 'o':
        break

    try:
        if sand[1]+1-y_range[0] == len(mappert):
            if not uno:
                print(f'part 1: {num}')
                uno = True
            mappert[sand[1] - y_range[0]][sand[0] - x_range[0]] = 'o'
            num += 1
            sand = 500, 0
        elif mappert[sand[1]+1-y_range[0]][sand[0]-x_range[0]] not in ('#', 'o'):
            sand = sand[0], sand[1]+1
        elif mappert[sand[1]+1-y_range[0]][sand[0]-x_range[0]-1] not in ('#', 'o'):
            sand = sand[0]-1, sand[1]+1
        elif mappert[sand[1]+1-y_range[0]][sand[0]-x_range[0]+1] not in ('#', 'o'):
            sand = sand[0]+1, sand[1]+1
        else:
            mappert[sand[1]-y_range[0]][sand[0]-x_range[0]] = 'o'
            num += 1
            sand = 500, 0
    except IndexError:
        break

for i in range(len(mappert)):
    for j in range(len(mappert[0])):
        if mappert[i][j] == '.':
            mappert[i][j] = 0
        if mappert[i][j] == '#':
            mappert[i][j] = 1
        if mappert[i][j] == 'o':
            mappert[i][j] = 2
plt.figure()
plt.imshow(mappert)
plt.show()
print(f'part 2: {num}')