from time import time

with open('input.txt') as infile:
    monkeys_notes = [row.strip() for row in infile.readlines()]

# test_input.txt
# == After round 10000 ==
# Monkey 0 inspected items 52166 times.
# Monkey 1 inspected items 47830 times.
# Monkey 2 inspected items 1938 times.
# Monkey 3 inspected items 52013 times
# monkey_business: 2713310158


class Monkey:
    def __init__(self, name, items, op, value, test_mod, if_true, if_false):
        self.name = name
        self.items = items
        self.op = op
        self.value = value
        self.test_mod = test_mod
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0


monkeys = []

start = time()

for i in range(0, len(monkeys_notes), 7):
    name, s_items, s_op, s_mod, s_true, s_false = monkeys_notes[i:i+6]
    items = [int(i) for i in s_items[16:].split(', ')]
    old, op, value = s_op[17:].split()
    if value == 'old':
        op = '^'
    else:
        value = int(value)
    test_mod = int(s_mod.split()[-1])
    if_true = int(s_true.split()[-1])
    if_false = int(s_false.split()[-1])
    monkeys.append(Monkey(name, items, op, value, test_mod, if_true, if_false))


common_multiple = 1
for money in monkeys:
    common_multiple *= money.test_mod

for i in range(10000):
    for monkey in monkeys:
        monkey.inspected += len(monkey.items)
        for item in monkey.items:
            if monkey.op == '+':
                w = item + monkey.value
            elif monkey.op == '*':
                w = item * monkey.value
            else:
                w = item * item
            w %= common_multiple
            if w % monkey.test_mod == 0:
                monkeys[monkey.if_true].items.append(w)
            else:
                monkeys[monkey.if_false].items.append(w)
            monkey.items = []

inspects = []

for monkey in monkeys:
    print(f'{monkey.name} inspected items {monkey.inspected} times.')
    inspects.append(monkey.inspected)

inspects.sort()

print(f'monkey_business: {inspects[-1] * inspects[-2]}')

print(f'time: {time() - start}')

# Monkey 0: inspected items 115025 times.
# Monkey 1: inspected items 93029 times.
# Monkey 2: inspected items 114545 times.
# Monkey 3: inspected items 114164 times.
# Monkey 4: inspected items 8590 times.
# Monkey 5: inspected items 30465 times.
# Monkey 6: inspected items 122693 times.
# Monkey 7: inspected items 122667 times.
# monkey_business: 15050382231