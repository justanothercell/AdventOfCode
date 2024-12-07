with open('input.txt') as infile:
    raw_equations = infile.read().strip().split('\n')

equations = []
for e in raw_equations:
    result, input = e.split(':')
    equations.append((int(result), [int(i) for i in input.strip().split(' ')]))

sum = 0

for (r, e) in equations:
    ops = 0 # binary digits, 0 <=> +, 1 <=> *
    solutions = 0
    while ops < 2**(len(e)-1):
        s = e[0]
        print(f'{e[0]}', end='')
        for i, n in enumerate(e[1:]):
            if ops & (1 << i) == 0:
                print(f' + {n}', end='')
                s += n
            else:
                print(f' * {n}', end='')
                s *= n
            if s > r:
                break
        if s == r:
            print(f' = {s}')
            solutions += 1
        else:
            print(f'\r', end='')
            print(f'                                                         ', end='')
            print(f'\r', end='')
        ops += 1
    if solutions > 0:
        print()
        sum += r

print(f'sum={sum}')
