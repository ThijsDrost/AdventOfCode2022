loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 7\input.txt'

with open(loc, 'r') as file:
    loc = []
    files = {}
    curr_loc = files
    file.readline()
    for line in file:
        line = line.removesuffix('\n')
        if line.startswith('$'):
            if line[2:4] == 'cd':
                if line[5:] == '..':
                    loc.pop(-1)
                else:
                    loc.append(line[5:])
                curr_loc = files
                for l in loc:
                    curr_loc = curr_loc[l]
            elif line[2:4] == 'ls':
                pass
            else:
                raise ValueError
        elif line.startswith('dir'):
            curr_loc[line[4:]] = {}
        else:
            curr_loc[line.split()[1]] = int(line.split()[0])


def dict_size(dictionary, size_value=100000):
    d_size = 0
    size_counter = 0
    totals = 0

    for key, value in dictionary.items():
        if isinstance(value, dict):
            num, total, extra_size, = dict_size(value, size_value)
            size_counter += num
            totals += total
            d_size += extra_size
        else:
            d_size += value

    if d_size < size_value:
        size_counter += 1
        totals += d_size
    # print(f'{size_counter},  {d_size}, {dictionary}')
    return size_counter, totals, d_size

print(vals := dict_size(files))

# %%
total_space = 70_000_000
needed_space = 30_000_000
to_free = needed_space - (total_space - vals[2])


def dict_size(dictionary, size_value, name):
    d_size = 0
    dict_dict = {}

    for key, value in dictionary.items():
        if isinstance(value, dict):
            dict_new, extra_size = dict_size(value, size_value, key)
            d_size += extra_size
            dict_dict.update(dict_new)
        else:
            d_size += value

    if d_size > size_value:
        dict_dict[name] = d_size
    return dict_dict, d_size


result = dict_size(files, to_free, '/')[0]
print(result[min(result, key=result.get)])
