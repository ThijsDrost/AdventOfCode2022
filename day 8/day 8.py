loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 8\input.txt'

with open(loc, 'r') as file:
    lines = [line.removesuffix('\n') for line in file]
    total = 0
    for i in range(1, len(lines[0])-1):
        for j in range(1, len(lines)-1):
            height = int(lines[i][j])
            for up in range(1, i+1):
                if height <= int(lines[i-up][j]):
                    break
            else:
                total += 1
                print(f'u: {i}, {j}')
                continue

            for down in range(1, len(lines[0])-i):
                if height <= int(lines[i+down][j]):
                    break
            else:
                total += 1
                print(f'd: {i}, {j}')
                continue

            for left in range(1, j+1):
                if height <= int(lines[i][j-left]):
                    break
            else:
                total += 1
                print(f'l: {i}, {j}')
                continue

            for right in range(1, len(lines)-j):
                if height <= int(lines[i][j+right]):
                    break
            else:
                total += 1
                print(f'r: {i}, {j}')
                continue

print(total)
total += 2*(len(lines[0])-1) + 2*(len(lines)-1)
print(total)

# %%
loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 8\input.txt'

max_val = 0
with open(loc, 'r') as file:
    lines = [line.removesuffix('\n') for line in file]
    for i in range(1, len(lines[0])-1):
        for j in range(1, len(lines)-1):
            height = int(lines[i][j])
            for up in range(1, i+1):
                if height <= int(lines[i-up][j]):
                    break
            v_up = up

            for down in range(1, len(lines[0])-i):
                if height <= int(lines[i+down][j]):
                    break
            v_down = down

            for left in range(1, j+1):
                if height <= int(lines[i][j-left]):
                    break
            v_left = left

            for right in range(1, len(lines)-j):
                if height <= int(lines[i][j+right]):
                    break
            v_right = right

            val = v_left*v_right*v_down*v_up
            if val > max_val:
                max_val = val
                # print(f'{i}, {j}: {val}')
                # print(f'{v_up}, {v_down}, {v_left}, {v_right}')

print(max_val)
