from functools import cmp_to_key
loc = r'input.txt'


def compare(val1, val2):
    if isinstance(val1, list) and isinstance(val2, list):
        for v1, v2 in zip(val1, val2):
            if (x := compare(v1, v2)) != 0:
                return x
        return compare(len(val1), len(val2))
    if isinstance(val1, int) and isinstance(val2, list):
        return compare([val1], val2)
    if isinstance(val1, list) and isinstance(val2, int):
        return compare(val1, [val2])
    if isinstance(val1, int) and isinstance(val2, int):
        if val1 > val2:
            return -1
        if val1 < val2:
            return 1
        return 0


total = 0
lines = []
with open(loc, 'r') as file:
    index = 1
    while True:
        if not (line := file.readline()):
            break
        exec('list1 = {}'.format(line.removesuffix("\n")))
        exec('list2 = {}'.format(file.readline().removesuffix("\n")))
        lines.append(list1)
        lines.append(list2)
        file.readline()
        if compare(list1, list2) == 1:
            total += index
        index += 1
print(total)

lines.append([[2]])
lines.append([[6]])
lines.sort(key=cmp_to_key(compare), reverse=True)
print((lines.index([[2]])+1)*(lines.index([[6]])+1))
