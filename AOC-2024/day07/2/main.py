with open('input.txt') as infile:
    raw_equations = infile.read().strip().split('\n')

equations = []
for e in raw_equations:
    result, input = e.split(':')
    equations.append((int(result), [int(i) for i in input.strip().split(' ')]))

sum = 0

for k, (r, e) in enumerate(equations):
    ops = ['+'] * (len(e) - 1) # ternary counter
    solutions = 0
    while True:
        s = e[0]
        for i, n in enumerate(e[1:]):
            if ops[i] == '+':
                s += n
            elif ops[i] == '||':
                s = int(str(s) + str(n))
            else:
                s *= n
            if s > r:
                break
        if s == r:
            solutions += 1
            break
        for i in range(len(ops)):
            if ops[i] == '+':
                ops[i] = '||'
                break
            elif ops[i] == '||':
                ops[i] = '*'
                break
            else:
                ops[i] = '+'
        else:
            break
    if solutions > 0:
        print(k, k / len(equations) * 100)
        sum += r

print(f'sum={sum}')
