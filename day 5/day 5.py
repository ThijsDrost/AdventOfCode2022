import re
loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 5\input.txt'

with open(loc, 'r') as file:
    first = file.readline().removesuffix('\n')
    row_num = int((len(first) + 1)/4) if (len(first) + 1) % 4 == 0 else ValueError
    rows = [[] for _ in range(row_num)]

    file.seek(0)
    for line in file:
        if line[1] == '1':
            break
        for i in range(row_num):
            rows[i] += [line[i*4+1]] if line[i*4+1] != ' ' else ''

    file.readline()
    for line in file:
        num, start, end = re.findall(r'\d+', line)
        num, start, end = int(num), int(start)-1, int(end)-1
        for i in range(num):
            rows[end] = [rows[start].pop(0)] + rows[end]

total = ''
for row in rows:
    total += row[0]
print(total)

# %%
with open(loc, 'r') as file:
    rows = [[] for _ in range(row_num)]

    for line in file:
        if line[1] == '1':
            break
        for i in range(row_num):
            rows[i] += [line[i*4+1]] if line[i*4+1] != ' ' else ''

    file.readline()
    for line in file:
        num, start, end = re.findall(r'\d+', line)
        num, start, end = int(num), int(start)-1, int(end)-1
        rows[end] = rows[start][:num] + rows[end]
        rows[start] = rows[start][num:]

total = ''
for row in rows:
    total += row[0]
print(total)
