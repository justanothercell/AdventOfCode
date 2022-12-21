with open('input.txt') as infile:
    monkeys = infile.readlines()

# root: 152
# monkeys = [
#     'root: pppw + sjmn',
#     'dbpl: 5',
#     'cczh: sllz + lgvd',
#     'zczc: 2',
#     'ptdq: humn - dvpt',
#     'dvpt: 3',
#     'lfqf: 4',
#     'humn: 5',
#     'ljgn: 2',
#     'sjmn: drzm * dbpl',
#     'sllz: 4',
#     'pppw: cczh / lfqf',
#     'lgvd: ljgn * ptdq',
#     'drzm: hmdt - zczc',
#     'hmdt: 32',
# ]

variables = {}
math_monkeys = {}
for m in monkeys:
    name, value = m.split(': ')
    math_monkeys[name] = value


def collect(collectable_monkeys):
    for name in collectable_monkeys:
        value = math_monkeys[name]
        to_be_collected = []
        s = value.split()
        if len(s) == 3:
            a, _, b = s
            if a not in variables:
                to_be_collected.append(a)
            if b not in variables:
                to_be_collected.append(b)
        if len(to_be_collected) > 0:
            collect(to_be_collected)
        e = eval(value, variables)
        variables[name] = e


collect(['root'])


print(f'root: {int(variables["root"])}')
# root: 49288254556480

