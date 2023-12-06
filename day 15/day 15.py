import re
import time

import numpy as np

loc = 'input.txt'
line_num = 2000000

s_b = []
with open(loc, 'r') as file:
    for line in file:
        sensor, beacon = line.removesuffix('\n').split(':')
        sensor_x = int(re.findall(r'x=(-?\d+)', sensor)[0])
        sensor_y = int(re.findall(r'y=(-?\d+)', sensor)[0])
        beacon_x = int(re.findall(r'x=(-?\d+)', beacon)[0])
        beacon_y = int(re.findall(r'y=(-?\d+)', beacon)[0])
        s_b.append(((sensor_x, sensor_y), abs(sensor_x-beacon_x)+abs(sensor_y-beacon_y)))

# %%
num = 0
inside = False
for sb in s_b:
    distance = abs(sb[0][0]-num)+abs(sb[0][1]-line_num)
    if distance < sb[1]:
        inside = True
        break
if not inside:
    raise Exception('not inside')


while True:
    for sb in s_b:
        distance = abs(sb[0][0]-num)+abs(sb[0][1]-line_num)
        if distance <= sb[1]:
            break
    else:
        upper = num
        break
    num += 1

num = 0
while True:
    for sb in s_b:
        distance = abs(sb[0][0] - num) + abs(sb[0][1] - line_num)
        if distance <= sb[1]:
            break
    else:
        lower = num
        break
    num -= 1
    # print(num)
print(upper-lower-2)

# %%
start = time.time()
sizes = 4_000
for i in range(100):
    for j in range(100):
        x, y = np.meshgrid(np.arange(sizes), np.arange(sizes))
        mappert = np.zeros((sizes, sizes), dtype=np.uint8)
        for sb in s_b:
            distance = abs(sb[0][0] - (x+sizes*i)) + abs(sb[0][1] - (y+sizes*j))
            mappert[distance <= sb[1]] = 1
        loc = np.argwhere(mappert == 0)
        if len(loc) != 0:
            break
        print(f'\r{i+(j+1)/100:.2f}% after {(time.time()-start)/60:.1f} minutes', end='')

print(4000000*loc[0, 1]+loc[0, 0])

