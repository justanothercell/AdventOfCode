from time import sleep
from itertools import combinations

with open('input.txt') as infile:
    raw_map = infile.read().strip().split('\n')

map = []
start_x, start_y = 0, 0
w, h = len(raw_map[0]), len(raw_map)

for y, row in enumerate(raw_map):
    r = []
    for x, c in enumerate(row):
        if c == '.':
            r.append(0)
        if c == '#':
            r.append(-1)
        if c == '^':
            r.append(0)
            start_x, start_y = x, y
    map.append(r)

saved_map = [ [x for x in row] for row in map ]
print(f'starting at {start_x} {start_y}')

dirs = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]

def simulate(gx, gy, m):
    dir = 0
    m[gy][gx] = 1 << dir # we start here!
    steps = 1
    while True:
        dx, dy = dirs[dir]
        gx += dx
        gy += dy
        if not (0 <= gx < w and 0 <= gy < h):
            return steps # we walked out of bounds
        if m[gy][gx] == -1:
            gx -= dx
            gy -= dy
            dir = (dir + 1) % 4
        else:
            mask = 1 << dir
            if m[gy][gx] & mask != 0:
                # we were already here, looking in the same direction
                steps = -1 # is a loop
                m[gy][gx] |= mask
                m[gy][gx] |= 1 << 4 # singal loop join position
                print(f'loop closed at {gx} {gy}')
                return steps
            else:
                if m[gy][gx] == 0:
                    steps += 1
                m[gy][gx] |= mask

steps = simulate(start_x, start_y, map)
print(f'steps={steps}')

loops = 0

for y in range(h):
    for x in range(w):
        if map[y][x] > 0: # we were here during normal patrol
            modified_map = [ [x for x in row] for row in saved_map ]
            modified_map[y][x] = -1
            if simulate(start_x, start_y, modified_map) == -1: # encountered a loop
                loops += 1
                print(f'Loop found with block at {x} {y}')
                if False:
                    for py in range(h):
                        for px in range(w):
                            if px == x and py == y:
                                print('O', end='')
                            elif modified_map[py][px] == -1:
                                print('#', end='')
                            elif modified_map[py][px] == 0:
                                print('.', end='')
                            elif modified_map[py][px] & (1 << 4) != 0:
                                print('K', end='')
                            elif modified_map[py][px] == 1 << 0:
                                print('^', end='')
                            elif modified_map[py][px] == 1 << 1:
                                print('>', end='')
                            elif modified_map[py][px] == 1 << 2:
                                print('v', end='')
                            elif modified_map[py][px] == 1 << 3:
                                print('<', end='')
                            else:
                                print('*', end='')
                        print()
print(f'loops={loops}')
