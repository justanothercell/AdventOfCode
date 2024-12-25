with open('input.txt') as infile:
    raw_vars, raw_gates = infile.read().strip().split('\n\n')

vars = {}
z_digits = 0
for rv in raw_vars.split('\n'):
    k, v = rv.split(': ')
    vars[k] = v == '1'

gates = {}
for rg in raw_gates.split('\n'):
    i, o = rg.split(' -> ')
    a, op, b = i.split(' ')
    if o.startswith('z'):
        z_digits += 1
    gates[o] = (op, a, b)

print(f'parsed {len(vars)} variables')
print(f'output has {z_digits} digits')
print(f'parsed {len(gates)} gates')

def beval(op, a, b):
    if a not in vars:
        vars[a] = beval(*gates[a])
    if b not in vars:
        vars[b] = beval(*gates[b])
    a, b = vars[a], vars[b]
    if op == 'AND':
        return a and b
    elif op == 'OR':
        return a or b
    elif op == 'XOR':
        return a ^ b
    else:
        assert False, f'Invalid gate op {op}'
result = 0
for i in range(z_digits):
    var = f'z{z_digits-1-i:02}'
    if var in vars:
        r = vars[var]
    else:
        r = beval(*gates[var])
    result <<= 1
    result |= r
    print('1' if r else '0', end='', flush=True)

print()
print(result)
