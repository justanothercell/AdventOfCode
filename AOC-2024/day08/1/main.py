import os
os.system('') # enable ansi escape codes

with open('input.txt') as infile:
    map = infile.read().strip().split('\n')

w, h = len(map[0]), len(map)
antinodes = set()
nodes = {}

for y in range(h):
    for x in range(w):
        c = map[y][x]
        if c == '.':
            continue
        if c not in nodes:
            nodes[c] = [(x, y)]
        else:
            for (ax, ay) in nodes[c]: # all partners
                dx = x - ax
                dy = y - ay
                if 0 <= x + dx < w and 0 <= y + dy < h:
                     antinodes.add((x + dx, y + dy))
                if 0 <= ax - dx < w and 0 <= ay - dy < h:
                    antinodes.add((ax - dx, ay - dy))
            nodes[c].append((x, y))
debug = True
if debug:
    for y in range(h):
        for x in range(w):
            c = map[y][x]
            if (x, y) in antinodes:
                print(f'\x1b[1;42m{c} \x1b[0m', end='')
            else:
                if x % 2 == y % 2:
                    print(f'\x1b[48;5;240m{c} \x1b[0m', end='')
                else:
                    print(f'\x1b[48;5;237m{c} \x1b[0m', end='')
        print()
    print()
    print(antinodes)

print(len(antinodes))
