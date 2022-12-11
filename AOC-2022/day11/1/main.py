with open('input.txt') as infile:
    monkeys_notes = [row.strip() for row in infile.readlines()]

# test_input.txt
# Monkey 0 inspected items 101 times.
# Monkey 1 inspected items 95 times.
# Monkey 2 inspected items 7 times.
# Monkey 3 inspected items 105 times.
# monkey_business: 10605


class Monkey:
    def __init__(self, name, items, op, test_mod, if_true, if_false):
        self.name = name
        self.items = items
        self.op = op
        self.test_mod = test_mod
        self.if_true = if_true
        self.if_false = if_false
        self.inspected = 0


monkeys = []

for i in range(0, len(monkeys_notes), 7):
    name, s_items, s_op, s_mod, s_true, s_false = monkeys_notes[i:i+6]
    items = [int(i) for i in s_items[16:].split(', ')]
    op = eval('lambda old: ' + s_op[17:])
    test_mod = int(s_mod.split()[-1])
    if_true = int(s_true.split()[-1])
    if_false = int(s_false.split()[-1])
    monkeys.append(Monkey(name, items, op, test_mod, if_true, if_false))


for i in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspected += 1
            w = monkey.op(item) // 3
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

# Monkey 0: inspected items 228 times.
# Monkey 1: inspected items 17 times.
# Monkey 2: inspected items 223 times.
# Monkey 3: inspected items 239 times.
# Monkey 4: inspected items 7 times.
# Monkey 5: inspected items 225 times.
# Monkey 6: inspected items 242 times.
# Monkey 7: inspected items 29 times.
# monkey_business: 57838
