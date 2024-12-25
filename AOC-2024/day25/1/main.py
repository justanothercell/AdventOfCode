with open('input.txt') as infile:
    raw_items = infile.read().strip().split('\n\n')

keys = {}
locks = {}
h = 7

for item in raw_items:
    rows = item.split('\n')
    pins = [0 for _ in range(len(rows[0]))]
    for row in rows:
        for i, c in enumerate(row):
            if c == '#':
                pins[i] += 1
    pins = tuple(pins)
    if rows[0][0] == '#': # is lock
        if pins not in locks:
            locks[pins] = 1
        else:
            locks[pins] += 1
    else: # is key
        if pins not in keys:
            keys[pins] = 1
        else:
            keys[pins] += 1

print(f'parsed {len(keys)} keys and {len(locks)} locks')
matches = 0
for lock, lc in locks.items():
    for key, kc in keys.items():
        if all(lp + kp <= h for lp, kp in zip(lock, key)):
            matches += lc * kc
print(f'{matches=}')
