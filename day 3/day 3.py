loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 3\input.txt'

total_value = 0
with open(loc, 'r') as file:
    for line in file:
        line = line.removesuffix('\n')
        first, second = line[:len(line)//2], line[len(line)//2:]
        letter = set(first).intersection(set(second)).pop()
        if letter.isupper():
            total_value += ord(letter) - 38
        else:
            total_value += ord(letter) - 96
print(total_value)

# %%
total_value = 0
with open(loc, 'r') as file:
    while True:
        sets = [
            set(file.readline().removesuffix('\n')),
            set(file.readline().removesuffix('\n')),
            set(file.readline().removesuffix('\n'))
        ]
        if not sets[0]:
            break
        letter = set.intersection(*sets).pop()
        if letter.isupper():
            total_value += ord(letter) - 38
        else:
            total_value += ord(letter) - 96
print(total_value)
