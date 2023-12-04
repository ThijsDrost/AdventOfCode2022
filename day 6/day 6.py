loc = r'C:\Users\20222772\PycharmProjects\AdventOfCode2022\day 6\input.txt'


def find_unique_length(loc, length):
    with open(loc, 'r') as file:
        line = file.readline()
        for index in range(length, len(line)):
            values = line[index-length:index]
            if len(set(values)) == length:
                print(index)
                break


find_unique_length(loc, 4)
find_unique_length(loc, 14)
