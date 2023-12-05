class Monkey:
    def __init__(self, items: list[int], change: str, div_test: int, throw_loc: tuple[int, int], worry_val: int,
                 mod_val: int = 0):
        self.items = items
        self.change = change
        self.div_test = div_test
        self.throw_loc = throw_loc
        self.inspected = 0
        self.mod_val = mod_val
        self.worry_val = worry_val

    def do(self, monkeys):
        self.inspected += len(self.items)
        while len(self.items) > 0:
            old = self.items.pop(0)
            item = [-1]
            exec(f'item[0] = {self.change}')
            item = item[0] // self.worry_val
            if self.mod_val != 0:
                item = item % self.mod_val

            if item % self.div_test == 0:
                monkeys[self.throw_loc[0]].give(item)
            else:
                monkeys[self.throw_loc[1]].give(item)

    def give(self, value):
        self.items.append(value)

def read_txt(loc: str, worry_val: int):
    with open(loc, 'r') as file:
        monkeys = []
        while True:
            file.readline()
            items = list(map(int, file.readline().removesuffix('\n').split(':')[1].split(',')))
            change = file.readline().removesuffix('\n').split('=')[1]
            test = int(file.readline().removesuffix('\n').split('by')[1])
            loc1 = int(file.readline().removesuffix('\n').split('monkey')[1])
            loc2 = int(file.readline().removesuffix('\n').split('monkey')[1])
            monkeys.append(Monkey(items, change, test, (loc1, loc2), worry_val))
            if not file.readline():
                break
    return monkeys


monkeys = read_txt('input.txt', 3)

for round in range(1, 21):
    for monkey in monkeys:
        monkey.do(monkeys)

monkeys = sorted(monkeys, key=lambda x: x.inspected)
print(monkeys[-1].inspected*monkeys[-2].inspected)

# %%
monkeys = read_txt('input.txt', 1)
val = 1
for monkey in monkeys:
    val *= monkey.div_test
for monkey in monkeys:
    monkey.mod_val = val

for round in range(10_000):
    for monkey in monkeys:
        monkey.do(monkeys)

monkeys = sorted(monkeys, key=lambda x: x.inspected)
print(monkeys[-1].inspected*monkeys[-2].inspected)
