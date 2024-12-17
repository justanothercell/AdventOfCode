with open('input.txt') as infile:
    map = [list(row) for row in infile.read().strip().split('\n')]

w, h = len(map[0]), len(map)

sx, sy = 1, h-2
ex, ey = w-2, 1

#          x   y   dx dy px    py    score
stack = [ (sx, sy, 1, 0, None, None, 0) ]

j = 0
while len(stack) > 0:
    if j % 100000 == 0:
        print(len(stack))
    j += 1
    x, y, dx, dy, px, py, score = stack.pop() # look at next move
    if map[y][x] == '#': # cannot move into wall
        continue
    if isinstance(map[y][x], str) and map[y][x] in '.ES': # first time visiting this tile
        map[y][x] = [(px, py, dx, dy, score)]
    else:
        new = False
        for i in range(len(map[y][x])):
            mpx, mpy, mdx, mdy, ms = map[y][x][i]
            if (mpx, mpy, mdx, mdy) == (px, py, dx, dy):
                if ms > score: # new lowest score
                    new = True
                    map[y][x][i] = (px, py, dx, dy, score)
                break # this thing already exists
        else: # no match
            new = True
            map[y][x].append((px, py, dx, dy, score))
        if not new:
            continue
    if x != ex or y != ey: # not at end
        stack.append((x + dx, y + dy, dx, dy, x, y, score + 1)) # move forward
        stack.append((x - dy, y - dx, -dy, -dx, x, y, score + 1001)) # move left
        stack.append((x + dy, y + dx, dy, dx, x, y, score + 1001)) # move right

print('pathfinding done, assembling...')

score = min([score for _, _, _, _, score in map[ey][ex]])

path = set()

def collect(x, y, dx, dy, sc):
    path.add((x, y))
    for (px, py, pdx, pdy, ps) in map[y][x]:
        if px is None:
            root_found = True
            continue
        if -pdx == dx and -pdy == dy: # can't do a 180
            continue
        if ps > sc:
            continue
        collect(px, py, pdx, pdy, ps)
collect(ex, ey, None, None, score)

for y in range(0, h, 2):
    for x in range(w):
        upper = '#' if y >= h else map[y][x]
        lower = '#' if y+1 >= h else map[y+1][x]
        if upper == '#':
            print('\x1b[48;2;220;0;0m', end='')
        elif (x, y) in path:
            print('\x1b[48;2;0;255;0m', end='')
        else:
           print(f'\x1b[48;2;30;30;30m', end='')
        if lower == '#':
            print('\x1b[38;2;220;0;0m', end='')
        elif (x, y+1) in path:
            print('\x1b[38;2;0;255;0m', end='')
        else:
           print(f'\x1b[38;2;30;30;30m', end='')
        print('▄\x1b[0m', end='')
    print()

print(f'{score=}')
print(f'len={len(path)}')
