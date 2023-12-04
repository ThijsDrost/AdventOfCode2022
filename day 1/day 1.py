loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 1\input.txt'

max_cal = 0
with open(loc, 'r') as file:
    cals = 0
    for line in file:
        if line != '\n':
            cals += int(line.removesuffix('\n'))
        else:
            max_cal = cals if cals > max_cal else max_cal
            cals = 0
print(max_cal)

# %%
max_cal = [0, 0, 0]
with open(loc, 'r') as file:
    cals = 0
    for line in file:
        if line != '\n':
            cals += int(line.removesuffix('\n'))
        else:
            if cals > max_cal[0]:
                max_cal[2] = max_cal[1]
                max_cal[1] = max_cal[0]
                max_cal[0] = cals
            elif cals > max_cal[1]:
                max_cal[2] = max_cal[1]
                max_cal[1] = cals
            elif cals > max_cal[2]:
                max_cal[2] = cals
            cals = 0
print(max_cal)
print(sum(max_cal))