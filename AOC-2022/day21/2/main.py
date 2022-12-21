with open('input.txt') as infile:
    monkeys = infile.readlines()

# left: [[4, '+', [2, '*', ['x', '-', 3]]], '/', 4]
# right: 150
# humn: ('x', 301)
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

math_monkeys['humn'] = 'x'

def collect(collectable_monkeys):
    is_humn = False
    for name in collectable_monkeys:
        if name == 'humn':
            is_humn = True
            continue
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
            if collect(to_be_collected):
                is_humn = True
                continue
        e = eval(value, {}, variables)
        variables[name] = e
    return is_humn


l, _, r = math_monkeys['root'].split()
collect([l, r])

print(math_monkeys)
print(variables)

def xpand(elem):
    if elem in variables:
        return variables[elem]
    m = math_monkeys[elem]
    s = m.split()
    if len(s) == 3:
        a, op, b = s
        return [xpand(a), op, xpand(b)]
    else:
        return m

left = xpand(l)
right = xpand(r)

print(f'left: {left}')
print(f'right: {right}')
# left: [20, '*', [[[7430909554588.0, '-', [[[[[[219, '+', [2, '*', [[[[[[[[[[[599.0, '+', [[2, '*', [278, '+', [[[2, '*', [[3, '*', [[[569.0, '+', [[[[[135, '+', [[[10, '*', [[[446, '+', [2, '*', [[[[[[[563.0, '+', [[[[[[[[301, '+', [[[[[7, '*', [109, '+', [[116, '+', [343, '+', [['x', '-', 838.0], '*', 17]]], '/', 5]]], '-', 797.0], '+', 909.0], '/', 2], '+', 636.0]], '/', 3], '-', 518], '*', 8], '+', 294], '*', 2], '-', 460], '/', 4]], '/', 3], '-', 159], '*', 5], '-', 282.0], '/', 2], '+', 297.0]]], '/', 8], '-', 24]], '-', 930.0], '/', 2]], '*', 2], '-', 453], '+', 310], '+', 24]], '/', 5], '+', 350]], '-', 732]], '+', 711.0], '/', 3]]], '-', 309]], '/', 6], '-', 300], '/', 12], '+', 825], '*', 67], '-', 458.0], '/', 2], '+', 400], '*', 2], '-', 869.0]]], '/', 7], '+', 22.0], '*', 2], '-', 738], '/', 10]], '/', 4], '+', 358.0]]
# right: 12133706805700.0


def rev(op):
    match op:
        case '+':
            return '-'
        case '-':
            return '+'
        case '*':
            return '/'
        case '/':
            return '*'



def solve(expr, value):
    if isinstance(expr, str):
        return expr, value
    if isinstance(expr, int | float):
        return expr, value
    a, op, b = expr
    if isinstance(b, int | float):
        value = eval(f'{value} {rev(op)} {b}')
        return solve(a, value)
    if isinstance(a, int | float):
        match op:
            case '+':
                return solve([b, '+', a], value)
            case '*':
                return solve([b, '*', a], value)
            case '-':
                return solve(b, a - value)
            case '/':
                return solve(b, a / value)
    return [a, op, b], value

res = solve(left, right)

print(f'humn: {res}')
# humn: ('x', 3558714869436.0)