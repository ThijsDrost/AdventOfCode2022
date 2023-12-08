from copy import deepcopy

loc = 'input.txt'

num_nonzero = 0
valves = {}
with open(loc, 'r') as file:
    for line in file:
        line = line.removesuffix('\n')
        uno, dos = line.split(';')
        name = uno.split('has')[0].removeprefix('Valve').strip()
        flow_rate = int(uno.split('rate=')[1])
        leading = dos.split('valve')[1].removeprefix('s').strip().split(', ')
        valves[name] = (flow_rate, leading)
        if flow_rate != 0:
            num_nonzero += 1

to_remove = []
for key, value in valves.items():
    if len(value[1]) == 2 and value[0] == 0:
        valves[value[1][0]][1].remove(key)
        valves[value[1][0]][1].append(value[1][1])
        valves[value[1][1]][1].remove(key)
        valves[value[1][1]][1].append(value[1][0])
        to_remove.append(key)
for key in to_remove:
    valves.pop(key)
print(len(valves), valves)


def step(time_left, f_rate, released, num_notzero, curr_valve, path, valves_dict):
    path.add(curr_valve)
    released += f_rate
    time_left -= 1
    vals, locss = [], []

    if (time_left == 0) or (num_notzero == 0):
        # print(time_left, num_notzero, f_rate, released)
        return released + time_left * f_rate, [curr_valve]

    if time_left < 0:
        raise ValueError('time_left < 0')

    # print(curr_valve, valves_dict[curr_valve][1], path, f_rate, time_left)

    if valves_dict[curr_valve][0] != 0:
        temp_valves = deepcopy(valves_dict)
        temp_valves[curr_valve] = (0, valves_dict[curr_valve][1])
        released_val, locs = step(time_left, f_rate + valves_dict[curr_valve][0], released, num_notzero - 1, curr_valve, set(), temp_valves)
        vals.append(released_val)
        locss.append(locs)

    for valve_name in valves_dict[curr_valve][1]:
        if valve_name not in path:
            released_val, locs = step(time_left, f_rate, released, num_notzero, valve_name, deepcopy(path), deepcopy(valves_dict))
            vals.append(released_val)
            locss.append(locs)

    if len(vals) == 0:
        return released + time_left * f_rate, [curr_valve]
    else:
        released_val = max(vals)
        locs = locss[vals.index(released_val)]
        locs.append(curr_valve)
        # print(locs)
        return released_val, locs


print(step(30, 0, 0, num_nonzero, 'AA', set(), valves))
