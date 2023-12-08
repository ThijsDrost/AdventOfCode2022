loc = 'input.txt'

nums = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

total = 0
with open(loc, 'r') as file:
    for line in file:
        num = 0
        for index, character in enumerate(line.removesuffix('\n')[::-1]):
            num += (5**index)*nums[character]
        total += num
print(total)

nums = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
num = ''
while total != 0:
    x = total % 5
    num += nums[total % 5]
    total //= 5
    if x in (3, 4):
        total += 1
result = num[::-1]
print(result)
