loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 4\input.txt'

total = 0
with open(loc, 'r') as file:
    for index, line in enumerate(file):
        first, second = line.removesuffix('\n').split(',')
        first_range = int(first.split('-')[0]), int(first.split('-')[1])
        second_range = int(second.split('-')[0]), int(second.split('-')[1])
        if first_range[0] <= second_range[0] <= first_range[1] or first_range[0] <= second_range[1] <= first_range[1]:
            total += 1
        elif second_range[0] <= first_range[0] <= second_range[1] or second_range[0] <= first_range[1] <= second_range[1]:
            total += 1
print(total)
