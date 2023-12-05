loc = 'input.txt'

c_values = [20, 60, 100, 140, 180, 220]
total = 0

with open(loc, 'r') as file:
    cycles = 1
    values = (1, 1, 1)
    busy = False
    sprite = ['.'] * 40
    sprite[0] = 'X'
    while True:
        cycles += 1
        if not busy:
            if not (line := file.readline()):
                break

            if line.startswith('noop'):
                values = (values[1], values[1])
            elif line.startswith('addx'):
                values = (values[0], values[0]+int(line.removesuffix('\n').split()[1]))
                busy = True
            else:
                raise ValueError(f'unknown instruction: {line}')
        else:
            busy = False
            values = (values[1], values[1])

        if cycles in c_values:
            # print(f'{cycles}: {values}')
            total += values[0]*cycles

        pixel_loc = cycles % 40
        if pixel_loc == 0:
            print(f'{"".join(sprite)}')
            sprite = ['.'] * 40
        if abs(values[0] - pixel_loc + 1) <= 1:
            sprite[pixel_loc-1] = 'X'
print(total)

