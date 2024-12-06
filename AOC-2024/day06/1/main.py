from time import sleep
from os import system
system('')

with open('input.txt') as infile:
    raw_map = infile.read().strip().split('\n')

map = []
gx, gy = 0, 0
dir = 0
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
            gx, gy = x, y
    map.append(r)

steps = 1
map[gy][gx] = 1 << dir # we start here!

print(f'starting at {gx} {gy}')
radius = 16
print(f'\n' * (radius * 2 + 1))

while True:
    print(f'\x1b[{radius*2+1}A')
    # sleep(0.01)
    for py in range(gy - radius, gy + radius):
        for px in range(gx - radius, gx + radius):
            if 0 <= px < w and 0 <= py < h:
                if map[py][px] == 0:
                    print('. ', end='')
                if map[py][px] == -1:
                    print('# ', end='')
                if map[py][px] > 0:
                    print('* ', end='')
            else:
                print('~ ', end='')
        print()
    if dir == 0:
        dx, dy = (0, -1)
    elif dir == 1:
        dx, dy = (1, 0)
    elif dir == 2:
        dx, dy = (0, 1)
    else:
        dx, dy = (-1, 0)
    gx += dx
    gy += dy
    if not (0 <= gx < w and 0 <= gy < h):
        break
    if map[gy][gx] == -1:
        gx -= dx
        gy -= dy
        dir = (dir + 1) % 4
    else:
        mask = 1 << dir
        if map[gy][gx] & mask != 0:
            # we were already here, looking in the same direction
            break
        else:
            if map[gy][gx] == 0:
                steps += 1
            map[gy][gx] |= mask

print(steps)
